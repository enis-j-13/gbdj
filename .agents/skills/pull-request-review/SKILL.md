---
name: pull-request-review
description: "Use to review a pull request or local diff against issue acceptance criteria, Python standards, security and tests. Produce severity-ranked, evidence-based findings and actionable recommendations."
---

# Pull Request Review

## Verantwortung und Ergebnis
Prüfe Änderungen und liefere einen nachvollziehbaren Review-Bericht mit
priorisierten Befunden. Ändere weder Code noch PR-Status; veröffentliche keine
Kommentare und merge nichts ohne einen zusätzlichen ausdrücklichen Auftrag.

## Ablauf
1. Lies AGENTS.md, PR-Beschreibung, zugehöriges Issue und Akzeptanzkriterien.
   Bestimme Base und Head sowie den tatsächlichen Diff. Bei lokalen Änderungen
   benenne Referenzen, uncommittete und untracked Dateien; bei fehlenden
   Produktinformationen kennzeichne die fachliche Prüflücke.
2. Lies geänderte Dateien im Kontext sowie betroffene Aufrufer und Tests.
   Prüfe nach der [Review-Methode](references/review.md) fachliche Korrektheit,
   Kriterien, Typisierung, Wartbarkeit, Fehlerbehandlung, Sicherheit,
   Testabdeckung und unbeabsichtigte Änderungen.
3. Verwende die bestehenden [Python-Standards](../../../docs/standards/python.md)
   und [Teststandards](../../../docs/standards/testing.md). Wiederhole deren
   Regeln nicht im Bericht, sondern begründe konkrete Abweichungen und Folgen.
4. Führe sichere relevante Checks aus, soweit die Umgebung es erlaubt. Führe
   unbekannten PR-Code nicht ungeprüft mit Secrets oder privilegiertem Zugriff aus.
   Trenne selbst beobachtete Ergebnisse von Angaben des Autors und ungetesteten Annahmen.
5. Klassifiziere Befunde als P0–P3 nach der Referenz. Nenne Ort, Auslöser,
   Auswirkung und konkrete Korrektur mit geeignetem Test. Vermeide spekulative
   Defekte und reine Stilpräferenzen ohne Bezug zum Standard.
6. Liefere den Bericht nach der [Vorlage](assets/review-report.md): schwerste
   Befunde zuerst, danach offene Fragen, Kriteriennachweise und Prüfergebnisse.
   Ohne belegte Befunde sage das ausdrücklich, nenne aber verbleibende Prüflücken.

## Abgrenzung
Eine fachliche Empfehlung ist keine GitHub-Freigabe. Berichte den Review-Umfang
und die konkret geprüfte Revision; behaupte keine Sicherheit außerhalb dieser Evidenz.
