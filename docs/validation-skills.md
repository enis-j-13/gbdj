# Validierung der vier Codex Skills

Stand: 31. Oktober 2026. Python 3.12.14, uv 0.12.23.

## Umfang und Ergebnisse

| Skill | Verantwortung | Ergebnis bei Verwendung |
| --- | --- | --- |
| `project-discovery` | Idee und Anforderungen klären | Product Brief mit Vision, Goal, Anforderungen, MVP, Risiken und Entscheidungsstatus |
| `backlog-refinement` | Anforderungen in kleine priorisierte Einträge zerlegen | Backlog, lokale Issue-Entwürfe und MVP-Roadmap |
| `python-issue-implementation` | Genau ein freigegebenes Issue umsetzen | Code, Tests, Kriteriennachweise und PR-Vorbereitung |
| `pull-request-review` | Änderungen im Kontext bewerten | Evidenzbasierter Bericht mit P0–P3-Befunden und Empfehlungen |

Alle Skills liegen unter `.agents/skills/<name>/SKILL.md`, enthalten YAML mit
`name` und `description` und verweisen auf eigene `references/` und `assets/`.
SKILL.md bleibt auf jeweils weniger als 80 Zeilen begrenzt. Die Issue-Vorlagen
für Epic, Story, Task und Bug liegen zentral in `.github/ISSUE_TEMPLATE/`.
Die Markdown-Bodies werden für lokale Entwürfe wiederverwendet, nicht dupliziert.

Der offizielle skill-creator war weder im verfügbaren Skill-Katalog noch in den
lokalen Codex-Skill-Verzeichnissen verfügbar; es wurde kein Ersatz-Skill angelegt.
AGENTS.md erhielt ausschließlich kurze Skill-Verweise. README wurde an den neuen
Stand angepasst. PyYAML ist ausschließlich eine Dev-Abhängigkeit für den Test;
Anwendungscode und bestehende Standards blieben unverändert.

## Ausgeführte Prüfungen

| Befehl | Ergebnis |
| --- | --- |
| `uv sync --locked` | Bestanden |
| `uv run ruff format --check .` | Bestanden |
| `uv run ruff check .` | Bestanden |
| `uv run mypy src` | Bestanden |
| `uv run mypy scripts` | Bestanden |
| `uv run pytest` | 47 bestanden, 0 fehlgeschlagen, 0 übersprungen |

Davon sind 22 neue Skill-Prüffälle: genau vier auffindbare Skills, valide
YAML-Metadaten und Namenszuordnung, kompakte Dateien, Referenz- und Asset-Struktur,
auflösbare lokale Markdown-Links, vier GitHub-Issue-Vorlagen sowie AGENTS-Verweise.
Negativfälle prüfen ungültiges YAML, fehlende oder doppelte Metadaten, falsche
Wertetypen, leere Beschreibungen, Namenskonflikte und defekte oder aus dem
Repository führende Links. pytest führt sie in der bestehenden CI automatisch aus.

Die bestehende Code-Coverage beträgt weiterhin 96,15 % für Anwendung und Bootstrap
einschließlich Branches. Sie misst keine Qualität von Skill-Anweisungen.

## Inhaltliche Prüfung und Grenzen

- Discovery trennt bestätigte Anforderungen, Vorschläge, Annahmen und offene Punkte.
- Refinement referenziert Scrum Refinement, Requirements Engineering, Functional
  Decomposition, Story Mapping, INVEST, Risikopriorisierung, DoR und DoD.
- Kriterien sind nummeriert und beobachtbar; Given–When–Then ist ausgeschlossen.
- Die Umsetzung erfordert genau ein identifizierbares, ausdrücklich freigegebenes
  Issue und verweist auf bestehende Python- und Teststandards.
- Reviews benennen Revision, Kriterien, reale Fundstellen, Auswirkungen und
  Korrekturvorschläge; eigene Prüfergebnisse und Autorangaben bleiben getrennt.
- Es wurden keine echten Issues oder externen Integrationen erzeugt. Die Skills
  autorisieren weder Issue-Veröffentlichung noch PR-Kommentare oder Merge nebenbei.
- Die Tests prüfen Struktur und Metadaten. Es wurde keine automatisierte Codex-
  Laufzeitauswertung der erzeugten Skills durchgeführt; die inhaltliche Prüfung
  erfolgte anhand der Anforderungen und verlinkten Methoden/Vorlagen.
- GitHub-API-Zugriff ist weiterhin mit `Forbidden` blockiert. Die Vorbereitung
  eines PR und der beauftragte Push nach main sind über Git davon unabhängig.
  Ein tatsächlicher GitHub-Actions-Lauf wird nicht als lokal nachgewiesen ausgegeben.
