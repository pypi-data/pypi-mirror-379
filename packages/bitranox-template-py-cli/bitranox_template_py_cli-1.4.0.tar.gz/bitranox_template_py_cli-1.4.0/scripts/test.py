from __future__ import annotations

import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path
from types import ModuleType

import click

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts._utils import (  # noqa: E402
    RunResult,
    bootstrap_dev,
    cmd_exists,
    get_project_metadata,
    run,
    sync_packaging,
)

PROJECT = get_project_metadata()
COVERAGE_TARGET = PROJECT.coverage_source
_TOML_MODULE: ModuleType | None = None


@click.command(help="Run lints, type-check, tests with coverage, and Codecov upload if configured")
@click.option("--coverage", type=click.Choice(["on", "auto", "off"]), default="on")
@click.option("--verbose", "-v", is_flag=True, help="Print executed commands before running them")
def main(coverage: str, verbose: bool) -> None:
    env_verbose = os.getenv("TEST_VERBOSE", "").lower()
    if not verbose and env_verbose in {"1", "true", "yes", "on"}:
        verbose = True

    def _run(
        cmd: list[str] | str,
        *,
        env: dict[str, str] | None = None,
        check: bool = True,
        capture: bool = True,
        label: str | None = None,
    ) -> RunResult:
        display = cmd if isinstance(cmd, str) else " ".join(cmd)
        if label and not verbose:
            click.echo(f"[{label}] $ {display}")
        if verbose:
            click.echo(f"  $ {display}")
            if env:
                overrides = {k: v for k, v in env.items() if os.environ.get(k) != v}
                if overrides:
                    env_view = " ".join(f"{k}={v}" for k, v in overrides.items())
                    click.echo(f"    env {env_view}")
        result = run(cmd, env=env, check=check, capture=capture)  # type: ignore[arg-type]
        if verbose and label:
            click.echo(f"    -> {label}: exit={result.code} out={bool(result.out)} err={bool(result.err)}")
        return result

    bootstrap_dev()

    click.echo("[0/4] Sync packaging (conda/brew/nix) with pyproject")
    sync_packaging()

    click.echo("[1/4] Ruff lint")
    _run(["ruff", "check", "."], check=False)  # type: ignore[list-item]

    click.echo("[2/4] Ruff format (apply)")
    _run(["ruff", "format", "."], check=False)  # type: ignore[list-item]

    click.echo("[3/4] Pyright type-check")
    _run(["pyright"], check=False)  # type: ignore[list-item]

    click.echo("[4/4] Pytest with coverage")
    for f in (".coverage", "coverage.xml"):
        try:
            Path(f).unlink()
        except FileNotFoundError:
            pass

    if coverage == "on" or (coverage == "auto" and (os.getenv("CI") or os.getenv("CODECOV_TOKEN"))):
        click.echo("[coverage] enabled")
        fail_under = _read_fail_under(Path("pyproject.toml"))
        with tempfile.TemporaryDirectory() as tmp:
            cov_file = Path(tmp) / ".coverage"
            click.echo(f"[coverage] file={cov_file}")
            env = os.environ | {"COVERAGE_FILE": str(cov_file)}
            pytest_result = _run(
                [
                    "python",
                    "-m",
                    "pytest",
                    f"--cov={COVERAGE_TARGET}",
                    "--cov-report=xml:coverage.xml",
                    "--cov-report=term-missing",
                    f"--cov-fail-under={fail_under}",
                    "-vv",
                ],
                env=env,
                capture=False,
                label="pytest",
            )
            if pytest_result.code != 0:
                click.echo("[pytest] failed; skipping commit and Codecov upload", err=True)
                raise SystemExit(pytest_result.code)
    else:
        click.echo("[coverage] disabled (set --coverage=on to force)")
        pytest_result = _run(["python", "-m", "pytest", "-vv"], capture=False, label="pytest-no-cov")  # type: ignore[list-item]
        if pytest_result.code != 0:
            click.echo("[pytest] failed; skipping commit and Codecov upload", err=True)
            raise SystemExit(pytest_result.code)

    _ensure_codecov_token()

    upload_result: RunResult | None = None
    uploaded = False

    if Path("coverage.xml").exists():
        try:
            commit_sha = _commit_before_upload()
        except RuntimeError as exc:
            click.echo(f"[git] {exc}", err=True)
            click.echo("[git] Aborting Codecov upload")
            return
        click.echo(f"[git] Prepared commit {commit_sha} for Codecov upload")
        click.echo("Uploading coverage to Codecov")
        codecov_name = f"local-{platform.system()}-{platform.python_version()}"
        if cmd_exists("codecov"):
            upload_result = _run(
                [
                    "codecov",
                    "-f",
                    "coverage.xml",
                    "-F",
                    "local",
                    "-n",
                    codecov_name,
                ],
                check=False,
                capture=False,
                label="codecov-upload-cli",
            )
        else:
            token = os.getenv("CODECOV_TOKEN")
            download = _run(
                ["curl", "-s", "https://codecov.io/bash", "-o", "codecov.sh"],
                capture=False,
                label="codecov-download",
            )
            if download.code == 0:
                upload_cmd = [
                    "bash",
                    "codecov.sh",
                    "-f",
                    "coverage.xml",
                    "-F",
                    "local",
                    "-n",
                    codecov_name,
                ]
                if token:
                    upload_cmd.extend(["-t", token])
                upload_result = _run(
                    upload_cmd,
                    check=False,
                    capture=False,
                    label="codecov-upload-fallback",
                )
            else:
                click.echo("[codecov] failed to download uploader", err=True)
            try:
                Path("codecov.sh").unlink()
            except FileNotFoundError:
                pass

        if upload_result is not None:
            if upload_result.code == 0:
                click.echo("[codecov] upload succeeded")
                uploaded = True
            else:
                click.echo(f"[codecov] upload failed (exit {upload_result.code})")
    else:
        click.echo("Skipping Codecov upload: coverage.xml not found")

    if Path("coverage.xml").exists():
        if uploaded:
            click.echo("All checks passed (coverage uploaded)")
        else:
            click.echo("Checks finished (coverage upload not confirmed)")
    else:
        click.echo("Checks finished (coverage.xml missing, upload skipped)")


def _get_toml_module() -> ModuleType:
    global _TOML_MODULE
    if _TOML_MODULE is not None:
        return _TOML_MODULE

    try:
        import tomllib as module  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        try:
            import tomli as module  # type: ignore[import-not-found, assignment]
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError("tomllib/tomli modules are unavailable. Install the 'tomli' package for Python < 3.11.") from exc

    _TOML_MODULE = module
    return module


def _read_fail_under(pyproject: Path) -> int:
    try:
        toml_module = _get_toml_module()
        data = toml_module.loads(pyproject.read_text())
        return int(data["tool"]["coverage"]["report"]["fail_under"])
    except Exception:
        return 80


def _commit_before_upload() -> str:
    """Create a local commit (allow-empty) before uploading coverage."""

    click.echo("[git] Creating local commit before Codecov upload")

    add_proc = subprocess.run(
        ["git", "add", "-A"],
        capture_output=True,
        text=True,
        check=False,
    )
    if add_proc.returncode != 0:
        message = add_proc.stderr.strip() or add_proc.stdout.strip() or "git add failed"
        raise RuntimeError(message)
    if add_proc.stdout.strip():
        click.echo(add_proc.stdout.strip())
    if add_proc.stderr.strip():
        click.echo(add_proc.stderr.strip(), err=True)

    commit_message = "test: auto commit before Codecov upload"
    commit_proc = subprocess.run(
        ["git", "commit", "--allow-empty", "-m", commit_message],
        capture_output=True,
        text=True,
        check=False,
    )
    if commit_proc.returncode != 0:
        message = commit_proc.stderr.strip() or commit_proc.stdout.strip() or "git commit failed"
        raise RuntimeError(message)
    if commit_proc.stdout.strip():
        click.echo(commit_proc.stdout.strip())
    if commit_proc.stderr.strip():
        click.echo(commit_proc.stderr.strip(), err=True)

    rev_proc = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    if rev_proc.returncode != 0:
        message = rev_proc.stderr.strip() or "failed to resolve commit SHA"
        raise RuntimeError(message)

    commit_sha = rev_proc.stdout.strip()
    click.echo(f"[git] Created commit {commit_sha}")
    return commit_sha


def _ensure_codecov_token() -> None:
    if os.getenv("CODECOV_TOKEN"):
        return
    env_path = Path(".env")
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        if key.strip() == "CODECOV_TOKEN":
            token = value.strip().strip("\"'")
            if token:
                os.environ.setdefault("CODECOV_TOKEN", token)
            break


if __name__ == "__main__":
    main()
