---
name: backlog-refinement
description: "Use to refine a Product Brief or existing backlog into prioritized epics, small stories and technical tasks with testable acceptance criteria, GitHub issue drafts and an MVP roadmap."
---

# Backlog Refinement

## Verantwortung und Ergebnis
Übersetze bestätigte Produktziele in ein umsetzbares Backlog. Ergebnisse:
`docs/product/backlog.md`, `docs/product/mvp-roadmap.md` und lokale
Issue-Entwürfe unter `docs/product/issues/`, sofern kein anderer Pfad vereinbart ist.

## Ablauf
1. Lies AGENTS.md, Product Brief, bestehendes Backlog und relevante Architektur.
   Erhalte IDs und bestätigten Scope. Fehlende Ziele werden als Klärungsbedarf
   behandelt; Vorschläge werden nicht zu bestätigten Anforderungen umetikettiert.
2. Verwende die [Refinement-Methode](references/refinement.md): Scrum Refinement,
   Requirements Engineering, funktionale Zerlegung und User Story Mapping.
3. Erzeuge Epics mit Outcome und Scope. Nutze Features nur bei begründeter
   zusätzlicher Bündelung. Schneide Stories nach durchgängigem Nutzen und INVEST;
   trenne technische Tasks von nutzerbezogenen Stories.
4. Formuliere eindeutige, nummerierte Akzeptanzkriterien mit beobachtbarem Ergebnis,
   Eingaben und relevanten Grenzen. Verwende keine Given–When–Then-Struktur.
5. Ordne Prioritäten mit Nutzen- und Risikobegründung, Abhängigkeiten und groben
   relativen Schätzungen zu. Dokumentiere Unsicherheit, DoR-Status und DoD-Nachweise.
6. Schreibe Entwürfe mit den zentralen GitHub-Vorlagen für
   [Epic](../../../.github/ISSUE_TEMPLATE/epic.md),
   [Story](../../../.github/ISSUE_TEMPLATE/story.md),
   [Task](../../../.github/ISSUE_TEMPLATE/task.md) und
   [Bug](../../../.github/ISSUE_TEMPLATE/bug.md).
   Übernimm nur den Markdown-Body, nicht die YAML-Metadaten, in Issue-Entwürfe.
7. Erstelle die priorisierte MVP-Abfolge mit der
   [Backlog- und Roadmap-Vorlage](assets/backlog-roadmap.md). Prüfe Traceability,
   Zyklen, zu große Stories und unbestätigte Einträge vor Übergabe.

## Freigabegrenze
Erzeuge ausschließlich lokale Markdown-Entwürfe. Erstelle oder veröffentliche
keine echten GitHub-Issues ohne ausdrückliche Freigabe für die konkreten Einträge.
Ein freigegebenes Backlog ist noch keine Implementierungsfreigabe für jedes Issue.
