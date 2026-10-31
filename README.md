# <!-- project-title -->GlobalStockBot (GBDJ)

GlobalStockBot ist eine geplante, erweiterbare Python-Trading-Plattform für
Aktien. Langfristig soll sie internationale Aktienmärkte, regelbasierte
Swing-Trading-Strategien, historische Auswertungen sowie Portfolio- und
Risikomanagement unterstützen. Freqtrade dient als funktionale Orientierung;
eine Übernahme seiner Architektur ist nicht beschlossen.

Das Projekt befindet sich in der Product Discovery. Der
[Product Brief](docs/product/product-brief.md) trennt bestätigte Anforderungen,
Vorschläge, Annahmen und offene Entscheidungen. Distribution und Python-Paket
heißen `gbdj`, der Produktname lautet GlobalStockBot.

**Sicherheitsgrenze:** Zunächst ausschließlich Paper-Trading. Es gibt noch keine
Trading-Funktionen und keine Brokeranbindung. Entwicklung und Tests dürfen keine
Echtgeld-Orders auslösen. Vollautomatischer Live-Handel erfordert eine ausdrückliche
spätere Freigabe und gehört nicht zum vorgeschlagenen MVP.

## Voraussetzungen

- Git und Python 3.12 als definierte Startversion
- [uv](https://docs.astral.sh/uv/getting-started/installation/), in CI Version 0.12.23
- Für Pull Requests: passende Repository-Berechtigungen

## Installation

```bash
uv python install 3.12
uv sync --locked
```

uv erstellt `.venv` und installiert das Projekt einschließlich der Dev-Gruppe.
`uv.lock` ist versioniert. Dependency-Änderungen erfolgen mit `uv add` bzw.
`uv add --dev`; Manifest und Lockfile werden gemeinsam geprüft und committed.
Für den aktuellen Projektstand sind keine Secrets oder laufenden Dienste nötig.
Codex Cloud verwendet das vorhandene Checkout; zusätzliche Worktrees sind nicht
nötig. In der aktuellen Cloud-Umgebung sind vor uv-Befehlen schreibbare Pfade nötig:

```bash
export UV_CACHE_DIR=/workspace/.cache/uv
export UV_PYTHON_INSTALL_DIR=/workspace/.local/share/uv/python
cd /workspace/gbdj
```

## Entwicklung und Qualitätsprüfungen

```bash
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked mypy src
uv run --locked mypy scripts
uv run --locked pytest
uv build
```

Zum Formatieren: `uv run ruff format .`. pytest misst auch Branch-Coverage mit
einer Mindestabdeckung von 85 %. GitHub Actions führt Installation,
Qualitätsprüfungen und Paketbau bei Pull Requests und Pushes auf `main` aus.
Arbeite auf einem eigenen Branch und lasse Änderungen per Pull Request prüfen;
kein automatischer Merge. Die Ergebnisse dieser Initialisierung stehen im
[Validierungsabschnitt des Product Briefs](docs/product/product-brief.md#validierung-dieses-auftrags).

Die technische Basis stammt aus der Python Project Factory. Das vorhandene
Skript wurde für diese Initialisierung verwendet:

```bash
python3 scripts/bootstrap_project.py --project-name gbdj --package-name gbdj
```

Die Initialisierung ist abgeschlossen. Eine Wiederholung mit denselben Namen
ändert nichts; das Skript ist kein Werkzeug zum späteren Umbenennen des Produkts.
Die bestehenden Skills unterstützen Discovery, Refinement, Issue-Umsetzung und
Review; siehe [AGENTS.md](AGENTS.md). Dieser Auftrag erzeugt ausschließlich die
Projektinitialisierung und den Product Brief; ein Backlog wird nicht angelegt.

## Struktur

| Pfad | Zweck |
| --- | --- |
| `src/gbdj/` | Initialisiertes Python-Paket mit Typinformationen |
| `tests/` | Smoke-Test und Tests der bestehenden Factory-Werkzeuge |
| `scripts/bootstrap_project.py` | Bestehendes Initialisierungsskript |
| `docs/product/product-brief.md` | Produktverständnis und offene Entscheidungen |
| `docs/standards/` | Dauerhafte Python- und Testkonventionen |
| `docs/architecture/decisions/` | Architecture Decision Records |
| `AGENTS.md` | Orientierung für Entwicklungsagenten |
| `.agents/skills/` | Bestehende Skills mit Methoden und Ergebnisvorlagen |
| `.github/` | CI und Pull-Request-Vorlage |

Siehe [Python-Standards](docs/standards/python.md),
[Teststandards](docs/standards/testing.md) und
[Toolchain-ADR](docs/architecture/decisions/0001-python-toolchain.md).
