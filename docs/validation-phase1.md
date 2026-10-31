# Phase 1: Implementierung und Validierung

Ausgeführt am 31. Oktober 2026 unter Linux mit Python 3.12.14 und uv 0.12.23.

## Umfang und Entscheidungen

- Das lokale und entfernte Repository enthielt zu Beginn weder Commits noch
  README oder .gitignore. Es wurden keine bestehenden Projektdateien ersetzt.
- `src`-Layout, Hatchling, PEP-621-Metadaten, PEP-735-Dev-Gruppe und uv-Lockfile.
- Python 3.12 als Startversion; keine Zusage für ungetestete spätere Python-Versionen.
- Ruff mit 88 Zeichen und NumPy-Docstrings; striktes mypy für Anwendung und Skripte.
- Bootstrap mit Vorabvalidierung, gezielten Markern, Konflikt- und Symlink-Schutz,
  Wiederholbarkeit sowie Wiederherstellung bei einem Schreibfehler.
- Standards, ADR, schlanke AGENTS.md, README, CI und Pull-Request-Vorlage.
- Keine Frameworks, Datenbanken, Docker-Dateien, Codex Skills, Issues oder Projects.

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| `uv sync --locked` | Erfolgreich |
| `uv run ruff format --check .` | Erfolgreich |
| `uv run ruff check .` | Erfolgreich |
| `uv run mypy src` | Erfolgreich |
| `uv run mypy scripts` | Erfolgreich |
| `uv run pytest` | 25 bestanden, 0 fehlgeschlagen, 0 übersprungen |
| pytest-cov inkl. Branches | 96,15 %, Mindestabdeckung 85 % erreicht |
| `uv build` | Wheel und Source-Distribution erfolgreich |
| Vollständiges umbenanntes Template | Alle obigen Qualitätsprüfungen erfolgreich |

Die temporäre Kopie wurde über die echte CLI als `example-analytics` mit Paket
`example_analytics` initialisiert. Der zweite Aufruf blieb ohne Änderungen.
`uv sync --locked --offline`, Ruff, mypy, alle 25 Tests und `uv build --offline`
bestanden anschließend. Die Tests prüfen zusätzlich ungültige Eingaben,
Zielkonflikte, fehlende und veränderte Marker, Symlinks, abweichende wiederholte
Namen und die Wiederherstellung nach einem simulierten Schreibfehler.

## Einschränkungen und externe Schritte

- GitHub Actions wurde lokal nachvollzogen; ein tatsächlicher entfernter CI-Lauf
  ist damit noch nicht nachgewiesen.
- `gh api repos/enis-j-13/python-project-factory` scheiterte mit `Forbidden`.
  PR-Erstellung, GitHub-seitiger Merge und Template-Einstellung benötigen
  funktionierenden API-Zugriff. Der Git-Transport ist davon unabhängig.
- Im Cloud-Konfigurationsentwurf wurden das getestete `install_script` und die
  zusätzliche Domain `api.github.com` gespeichert. Dieser Entwurf aktiviert oder
  veröffentlicht die Konfiguration nicht automatisch.
- Vor Nutzung von **Use this template** muss das Repository auf GitHub als
  Template markiert sein. Diese Einstellung ist kein Repository-Dateiformat.
- Der Bootstrap ist für die Initialisierung vor eigenen Strukturänderungen
  gedacht und setzt voraus, dass keine parallelen Dateiedits stattfinden.
- Ein Betriebssystemabbruch oder ein dauerhaft defektes Dateisystem kann keine
  transaktionale Wiederherstellung garantieren; wichtige Änderungen gehören in Git.
