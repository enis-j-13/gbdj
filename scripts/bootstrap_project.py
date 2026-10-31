"""Initialize the template without overwriting unrelated project files."""

import argparse
import keyword
import re
import sys
import tomllib
from pathlib import Path


def validate_names(project_name: str, package_name: str) -> None:
    """Validate a canonical distribution name and a Python package identifier.

    Parameters
    ----------
    project_name : str
        Lowercase distribution name, with optional single hyphens.
    package_name : str
        ASCII Python identifier used for the importable package.

    Raises
    ------
    ValueError
        If either name is invalid or still contains a template placeholder.
    """
    if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", project_name):
        raise ValueError("Project name must use lowercase letters, digits and hyphens.")
    if (
        not re.fullmatch(r"[a-z][a-z0-9_]*", package_name)
        or keyword.iskeyword(package_name)
        or keyword.issoftkeyword(package_name)
        or package_name in sys.stdlib_module_names
    ):
        raise ValueError("Package name must be a non-reserved lowercase identifier.")
    if project_name == "python-project-factory" or package_name == "project_name":
        raise ValueError("Choose new names instead of the template placeholders.")


def run_bootstrap(root: Path, project_name: str, package_name: str) -> bool:
    """Initialize a pristine template, or return False for an identical repeat.

    Only explicitly managed text files and the placeholder package directory are
    changed. All names, markers and paths are checked before the first write.
    Concurrent edits during initialization are not supported.
    """
    validate_names(project_name, package_name)
    root = root.resolve()
    paths = [Path(name) for name in ("pyproject.toml", "uv.lock", "README.md")]
    paths.append(Path("tests/test_smoke.py"))
    source = root / "src/project_name"
    target = root / "src" / package_name
    for path in [*(root / item for item in paths), source, target]:
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f"Unsafe path: {path.relative_to(root)}")
        for parent in path.relative_to(root).parents:
            if (root / parent).is_symlink():
                raise ValueError(f"Symlink parent: {parent}")

    contents = {path: (root / path).read_text(encoding="utf-8") for path in paths}
    config = tomllib.loads(contents[Path("pyproject.toml")])
    current_project = config["project"]["name"]
    current_package = config["tool"]["project-factory"]["package"]
    if current_project == project_name and current_package == package_name:
        if not target.is_dir() or source.exists():
            raise ValueError("Existing initialization is inconsistent; inspect src/.")
        return False
    if current_project != "python-project-factory" or current_package != "project_name":
        raise ValueError("Already initialized with different names; no files changed.")
    if not source.is_dir() or target.exists():
        raise ValueError("Package source missing or target already exists.")

    replacements = {
        Path("pyproject.toml"): {
            'name = "python-project-factory"': f'name = "{project_name}"',
            'packages = ["src/project_name"]': f'packages = ["src/{package_name}"]',
            'package = "project_name"': f'package = "{package_name}"',
        },
        Path("uv.lock"): {
            'name = "python-project-factory"': f'name = "{project_name}"',
        },
        Path("README.md"): {
            "<!-- project-title -->Python Project Factory v1.0": (
                f"<!-- project-title -->{project_name}"
            ),
            "`src/project_name/`": f"`src/{package_name}/`",
        },
        Path("tests/test_smoke.py"): {
            'import_module("project_name")': f'import_module("{package_name}")',
        },
    }
    updated: dict[Path, str] = {}
    for path, markers in replacements.items():
        text = contents[path]
        for old, new in markers.items():
            if text.count(old) != 1:
                raise ValueError(
                    f"Expected exactly one template marker in {path}: {old}"
                )
            text = text.replace(old, new)
        updated[path] = text

    # Restore original contents and location if a filesystem operation fails.
    source.rename(target)
    try:
        for path, text in updated.items():
            (root / path).write_text(text, encoding="utf-8")
    except OSError:
        for path, text in contents.items():
            (root / path).write_text(text, encoding="utf-8")
        target.rename(source)
        raise
    return True


def run_cli() -> int:
    """Parse command-line arguments and report initialization failures."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--package-name", required=True)
    args = parser.parse_args()
    try:
        changed = run_bootstrap(
            Path(__file__).resolve().parents[1], args.project_name, args.package_name
        )
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Initialization failed: {error}\n")
    print("Project initialized." if changed else "Already initialized; no changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())
