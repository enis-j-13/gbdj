# Orientierung für Entwicklungsagenten

## Konventionen
- Python 3.12 ist die definierte Startversion; siehe `.python-version`.
- Verwende das bestehende Checkout; jede Cloud-Aufgabe ist bereits isoliert.
- Erzeuge zusätzliche Worktrees nur auf ausdrücklichen Wunsch.
- Anwendungscode gehört nach `src/`, Tests nach `tests/`.
- Verwende uv und versioniere `uv.lock` bei Dependency-Änderungen.
- Halte Änderungen klein, nachvollziehbar und auf den Auftrag begrenzt.
- Befolge [Python-Standards](docs/standards/python.md).
- Befolge [Teststandards](docs/standards/testing.md).
- Dokumentiere wesentliche Architekturentscheidungen als ADR.

## Skills
- Idee und Product Brief: [project-discovery](.agents/skills/project-discovery/SKILL.md).
- Backlog und Issue-Entwürfe: [backlog-refinement](.agents/skills/backlog-refinement/SKILL.md).
- Ein freigegebenes Issue: [python-issue-implementation](.agents/skills/python-issue-implementation/SKILL.md).
- Änderungsprüfung: [pull-request-review](.agents/skills/pull-request-review/SKILL.md).

## Qualitätsprüfungen
- Installiere mit `uv sync --locked`.
- Prüfe `uv run ruff format --check .` und `uv run ruff check .`.
- Prüfe `uv run mypy src` und `uv run mypy scripts`.
- Führe `uv run pytest` aus; beachte die Coverage-Untergrenze.
- Prüfe die Paketierbarkeit bei Packaging-Änderungen mit `uv build`.
- Melde ausgeführte, fehlgeschlagene und nicht ausgeführte Prüfungen getrennt.

## GitHub-Workflow
- Arbeite für Änderungen auf einem eigenen Branch und erstelle einen Pull Request.
- Beschreibe Problem, Verhalten und tatsächliche Validierung im Pull Request.
- Merge nur mit Auftrag und unter Beachtung der Repository-Schutzregeln.
- Erhalte bestehende Nutzeränderungen und vermeide erzwungene Pushes.

## Sicherheit
- Committe keine Secrets, Zugangsdaten oder lokalen Umgebungsdateien.
- Gib geheime Werte weder in Logs noch in Dokumentation aus.
- Behalte TLS-, Signatur- und Prüfsummenvalidierung bei.
- Validiere Eingaben an Systemgrenzen und verwende konkrete Fehlermeldungen.
