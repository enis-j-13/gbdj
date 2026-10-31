import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
SKILL_NAMES = (
    "project-discovery",
    "backlog-refinement",
    "python-issue-implementation",
    "pull-request-review",
)
ISSUE_TYPES = ("epic", "story", "task", "bug")


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing opening frontmatter delimiter")
    header, separator, body = text[4:].partition("\n---\n")
    if not separator or not body.strip():
        raise ValueError("Missing closing delimiter or Markdown body")
    try:
        data = yaml.safe_load(header)
        node = yaml.compose(header)
    except yaml.YAMLError as error:
        raise ValueError("Invalid YAML frontmatter") from error
    if not isinstance(data, dict) or not isinstance(node, yaml.MappingNode):
        raise ValueError("Frontmatter must be a mapping")
    if len(node.value) != len(data):
        raise ValueError("Duplicate metadata keys")
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in data.items()):
        raise ValueError("Metadata values must be strings")
    return data


def validate_skill_metadata(text: str, expected_name: str) -> None:
    metadata = read_frontmatter(text)
    if set(metadata) != {"name", "description"}:
        raise ValueError("Skills require exactly name and description")
    name = metadata["name"]
    if (
        name != expected_name
        or len(name) > 64
        or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
    ):
        raise ValueError("Invalid skill name or directory mismatch")
    description = metadata["description"]
    if not description.strip() or len(description) > 1024:
        raise ValueError("Missing or oversized description")
    if "<" in description or ">" in description:
        raise ValueError("Description must not contain angle brackets")


def validate_local_links(document: Path, root: Path) -> None:
    text = document.read_text(encoding="utf-8")
    for link in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", text):
        if link.startswith(("https://", "http://", "#")):
            continue
        target = (document.parent / link.split("#", 1)[0]).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            raise ValueError(f"Broken or escaping local link in {document}: {link}")


def test_exactly_four_skills_are_discoverable() -> None:
    assert {path.parent.name for path in SKILLS.glob("*/SKILL.md")} == set(SKILL_NAMES)
    assert {path.name for path in SKILLS.iterdir()} == set(SKILL_NAMES)


@pytest.mark.parametrize("name", SKILL_NAMES)
def test_skill_structure_metadata_and_links(name: str) -> None:
    folder = SKILLS / name
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    validate_skill_metadata(text, name)
    assert len(text.splitlines()) <= 80, "Keep SKILL.md compact"
    for subdirectory in ("references", "assets"):
        assert list((folder / subdirectory).glob("*.md"))
    for document in folder.rglob("*.md"):
        validate_local_links(document, ROOT)


@pytest.mark.parametrize("issue_type", ISSUE_TYPES)
def test_github_issue_template_metadata_and_sections(issue_type: str) -> None:
    document = ROOT / ".github/ISSUE_TEMPLATE" / f"{issue_type}.md"
    text = document.read_text(encoding="utf-8")
    metadata = read_frontmatter(text)
    assert set(metadata) == {"name", "about", "title", "labels", "assignees"}
    assert metadata["name"].lower() == issue_type
    assert metadata["about"].strip()
    assert metadata["title"].startswith(f"[{metadata['name']}]")
    assert "AC-1:" in text
    assert "Priorität" in text and "Abhängigkeiten" in text and "Größe" in text
    assert "Definition of Ready" in text and "Definition of Done" in text
    assert "Given–When–Then" not in text


def test_agent_skill_links_are_present_and_resolve() -> None:
    document = ROOT / "AGENTS.md"
    text = document.read_text(encoding="utf-8")
    for name in SKILL_NAMES:
        assert f".agents/skills/{name}/SKILL.md" in text
    validate_local_links(document, ROOT)


@pytest.mark.parametrize(
    "text",
    [
        "name: sample\n",
        "---\nname: sample\n",
        "---\nname: [broken\n---\n# Body\n",
        "---\n- sample\n---\n# Body\n",
        "---\nname: sample\nname: other\n---\n# Body\n",
        "---\nname: 12\ndescription: test\n---\n# Body\n",
        "---\nname: sample\n---\n# Body\n",
        "---\nname: other\ndescription: test\n---\n# Body\n",
        "---\nname: sample\ndescription: ''\n---\n# Body\n",
        "---\nname: sample\ndescription: '<tag>'\n---\n# Body\n",
    ],
)
def test_invalid_metadata_is_rejected(text: str) -> None:
    with pytest.raises(ValueError):
        validate_skill_metadata(text, "sample")


@pytest.mark.parametrize("link", ["missing.md", "../outside.md"])
def test_invalid_local_links_are_rejected(tmp_path: Path, link: str) -> None:
    document = tmp_path / "SKILL.md"
    document.write_text(f"[Reference]({link})", encoding="utf-8")
    with pytest.raises(ValueError, match="Broken or escaping"):
        validate_local_links(document, tmp_path)
