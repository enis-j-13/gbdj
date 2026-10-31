import importlib.util
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "bootstrap_project", ROOT / "scripts/bootstrap_project.py"
)
assert SPEC is not None and SPEC.loader is not None
bootstrap = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bootstrap)


@pytest.fixture
def template(tmp_path: Path) -> Path:
    for name in ("pyproject.toml", "uv.lock", "README.md"):
        shutil.copy2(ROOT / name, tmp_path / name)
    for name in ("src", "scripts"):
        shutil.copytree(
            ROOT / name, tmp_path / name, ignore=shutil.ignore_patterns("__pycache__")
        )
    (tmp_path / "tests").mkdir()
    shutil.copy2(ROOT / "tests/test_smoke.py", tmp_path / "tests/test_smoke.py")
    return tmp_path


def get_snapshot(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }


def test_initialization_and_repeat(template: Path) -> None:
    # This suite stays useful in generated projects as a no-op initialization test.
    config = tomllib.loads((template / "pyproject.toml").read_text())
    if config["project"]["name"] != "python-project-factory":
        assert not bootstrap.run_bootstrap(
            template,
            config["project"]["name"],
            config["tool"]["project-factory"]["package"],
        )
        return
    (template / "notes.txt").write_text("keep me")
    assert bootstrap.run_bootstrap(template, "weather-tools", "weather_tools")
    assert not (template / "src/project_name").exists()
    assert (template / "src/weather_tools/__init__.py").is_file()
    config = tomllib.loads((template / "pyproject.toml").read_text())
    assert config["project"]["name"] == "weather-tools"
    assert config["tool"]["hatch"]["build"]["targets"]["wheel"]["packages"] == [
        "src/weather_tools"
    ]
    assert (template / "notes.txt").read_text() == "keep me"
    before = get_snapshot(template)
    assert not bootstrap.run_bootstrap(template, "weather-tools", "weather_tools")
    assert get_snapshot(template) == before
    subprocess.run(["uv", "lock", "--check", "--offline"], cwd=template, check=True)
    subprocess.run(["uv", "sync", "--locked", "--offline"], cwd=template, check=True)
    subprocess.run(
        ["uv", "run", "--offline", "python", "-c", "import weather_tools"],
        cwd=template,
        check=True,
    )


@pytest.mark.parametrize(
    ("project", "package"),
    [
        ("../escape", "valid"),
        ("Upper", "valid"),
        ("a--b", "valid"),
        ("", "valid"),
        ("valid", "class"),
        ("valid", "match"),
        ("valid", "os"),
        ("valid", "../escape"),
        ("valid", "bad-name"),
        ("valid", "2bad"),
        ("valid", "Ünicode"),
        ("python-project-factory", "valid"),
        ("valid", "project_name"),
    ],
)
def test_invalid_names_leave_files_unchanged(
    template: Path, project: str, package: str
) -> None:
    before = get_snapshot(template)
    with pytest.raises(ValueError):
        bootstrap.run_bootstrap(template, project, package)
    assert get_snapshot(template) == before


@pytest.fixture
def pristine(template: Path) -> Path:
    # Recreate the managed markers for bootstrap tests in generated projects too.
    config = tomllib.loads((template / "pyproject.toml").read_text())
    project = config["project"]["name"]
    package = config["tool"]["project-factory"]["package"]
    if package != "project_name":
        (template / "src" / package).rename(template / "src/project_name")
        for name in ("pyproject.toml", "uv.lock", "README.md", "tests/test_smoke.py"):
            path = template / name
            text = path.read_text().replace(project, "python-project-factory")
            text = text.replace(package, "project_name")
            text = text.replace(
                "<!-- project-title -->python-project-factory",
                "<!-- project-title -->Python Project Factory v1.0",
            )
            path.write_text(text)
    return template


@pytest.mark.parametrize("conflict", ["target", "marker", "source", "symlink"])
def test_preflight_conflicts_do_not_change_files(pristine: Path, conflict: str) -> None:
    if conflict == "target":
        (pristine / "src/weather_tools").mkdir()
        (pristine / "src/weather_tools/important.txt").write_text("keep")
    elif conflict == "marker":
        (pristine / "tests/test_smoke.py").write_text("# user edited this file")
    elif conflict == "source":
        shutil.rmtree(pristine / "src/project_name")
    else:
        path = pristine / "README.md"
        path.rename(pristine / "original.md")
        path.symlink_to(pristine / "original.md")
    before = get_snapshot(pristine)
    with pytest.raises(ValueError):
        bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")
    assert get_snapshot(pristine) == before


def test_different_names_are_rejected(pristine: Path) -> None:
    bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")
    before = get_snapshot(pristine)
    with pytest.raises(ValueError, match="different names"):
        bootstrap.run_bootstrap(pristine, "other-project", "other_package")
    assert get_snapshot(pristine) == before


def test_inconsistent_repeat_is_rejected(pristine: Path) -> None:
    bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")
    (pristine / "src/project_name").mkdir()
    with pytest.raises(ValueError, match="inconsistent"):
        bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")


def test_symlink_parent_is_rejected(pristine: Path) -> None:
    (pristine / "tests").rename(pristine / "actual_tests")
    (pristine / "tests").symlink_to(pristine / "actual_tests", target_is_directory=True)
    before = get_snapshot(pristine)
    with pytest.raises(ValueError, match="Symlink parent"):
        bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")
    assert get_snapshot(pristine) == before


def test_write_failure_restores_template(
    pristine: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    before = get_snapshot(pristine)
    original = Path.write_text
    failed = False

    def write_once_failure(path: Path, text: str, encoding: str = "utf-8") -> int:
        nonlocal failed
        if path.name == "README.md" and not failed:
            failed = True
            raise OSError("simulated write failure")
        return original(path, text, encoding=encoding)

    monkeypatch.setattr(Path, "write_text", write_once_failure)
    with pytest.raises(OSError, match="simulated"):
        bootstrap.run_bootstrap(pristine, "weather-tools", "weather_tools")
    assert get_snapshot(pristine) == before


def test_cli_success_and_repeat(
    pristine: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        bootstrap, "__file__", str(pristine / "scripts/bootstrap_project.py")
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "bootstrap_project.py",
            "--project-name",
            "weather-tools",
            "--package-name",
            "weather_tools",
        ],
    )
    assert bootstrap.run_cli() == 0
    assert "Project initialized" in capsys.readouterr().out
    assert bootstrap.run_cli() == 0
    assert "Already initialized" in capsys.readouterr().out


def test_cli_invalid_input(pristine: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(pristine / "scripts/bootstrap_project.py"),
            "--project-name",
            "../bad",
            "--package-name",
            "good",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Initialization failed" in result.stderr
