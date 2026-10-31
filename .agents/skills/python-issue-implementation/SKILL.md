---
name: python-issue-implementation
description: "Use when exactly one GitHub issue is explicitly approved for implementation. Analyze its criteria and architecture, implement Python changes with tests, run quality checks and prepare a pull request."
---

# Python Issue Implementation

## Verantwortung und Ergebnis
Implementiere genau ein ausdrücklich freigegebenes GitHub Issue pro Auftrag.
Ergebnis: begrenzter Code-Diff, automatisierte Tests und ein prüfbarer PR-Entwurf.
Kein Backlog-Refinement, keine automatische Umsetzung weiterer Issues.

## Ablauf
1. Lies AGENTS.md und das konkrete Issue mit ID/URL, Beschreibung und
   Akzeptanzkriterien. Prüfe die ausdrückliche Umsetzungsfreigabe. Status oder
   Labels allein sind keine Freigabe. Bei mehreren Issues zuerst eines klären.
   Fehlt Zugriff, nutze einen bereitgestellten Issue-Auszug mit nachvollziehbarer
   ID und Stand; erfinde keine Inhalte oder erfüllten Kriterien.
2. Prüfe Kriterien, Scope, Abhängigkeiten und offene Fragen. Kläre blockierende
   Lücken vor davon abhängigen Änderungen. Erweitere den Auftrag nicht stillschweigend.
3. Untersuche bestehende Architektur, Datenflüsse, Tests und Git-Änderungen.
   Erhalte Nutzeränderungen und verwende den bestehenden Checkout.
4. Erstelle einen kleinen Plan aus betroffenen Komponenten, Änderungen und
   kriterienspezifischen Prüfungen. Nutze bei Bedarf die
   [Umsetzungs-Checkliste](references/implementation.md).
5. Implementiere nach den [Python-Standards](../../../docs/standards/python.md)
   und ergänze Tests nach den [Teststandards](../../../docs/standards/testing.md).
   Nutze vorhandene Muster und begründe neue Dependencies oder Architekturänderungen.
6. Führe `uv sync --locked`, `uv run ruff format --check .`,
   `uv run ruff check .`, `uv run mypy src`, `uv run mypy scripts` und
   `uv run pytest` aus. Ergänze erforderliche funktionale Prüfungen; bei
   Packaging-Änderungen auch `uv build`. Behebe auftragsbedingte Fehler und prüfe erneut.
7. Prüfe den Diff auf Scope und Secrets. Fasse erfüllte Kriterien mit Nachweisen,
   Änderungen, Risiken sowie bestandene, fehlgeschlagene und nicht ausgeführte
   Checks mit der [Ergebnisvorlage](assets/implementation-report.md) zusammen.
8. Bereite Branch und PR-Beschreibung nach der
   [PR-Vorlage](../../../.github/PULL_REQUEST_TEMPLATE.md) vor. Verlinke genau das
   beauftragte Issue. Push, PR-Veröffentlichung, Merge und Issue-Schließung erfolgen
   nur, wenn der Auftrag sie umfasst; die Vorbereitung allein autorisiert sie nicht.
