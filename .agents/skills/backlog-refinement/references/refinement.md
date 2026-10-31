# Refinement-Methode

## Vom Ziel zu kleinen Einträgen
1. Requirements Engineering: Ziele, Stakeholder, Quellen, Begriffe und Constraints
   prüfen. Jede Story auf bestätigte Anforderungs-IDs zurückführen; unbelegte Ideen
   als Vorschläge führen. Widersprüche vor einer Ready-Einstufung klären.
2. User Story Mapping: Nutzeraktivitäten als Backbone ordnen, einzelne Schritte
   darunter abbilden und horizontale Release-Schnitte für durchgängige Abläufe bilden.
3. Functional Decomposition: Fähigkeiten in beobachtbare Teilfähigkeiten zerlegen.
   Epics erhalten ein Ziel und eine Abschlussbedingung. Eine Feature-Ebene nur
   ergänzen, wenn ein Epic mehrere fachlich zusammengehörige Story-Gruppen enthält.
4. INVEST prüfen: Independent, Negotiable, Valuable, Estimable, Small, Testable.
   Abhängigkeiten nicht verstecken, sondern reduzieren oder explizit dokumentieren.
   Stories nach einfachen Fällen, Datenvarianten oder fachlichen Regeln schneiden;
   nicht ausschließlich nach Datenbank-, API- und UI-Schichten.
5. Scrum Refinement fortlaufend betreiben: obere Einträge detaillierter pflegen,
   neue Erkenntnisse einarbeiten und Reihenfolge anpassen. Weder feste Refinement-
   Zeremonie noch Zusagen zu Sprint-Umfang oder Lieferterminen erfinden.

## Kriterien und Beispiele
Akzeptanzkriterien beschreiben fachlich überprüfbare Ergebnisse, keine bloße
Aktivitätenliste. Beispiel einer Import-Story:
- AC-1: Eine UTF-8-CSV mit den Pflichtspalten wird vollständig eingelesen; die
  Ergebnisanzahl entspricht der Zahl gültiger Datenzeilen im Testdatensatz.
- AC-2: Bei fehlender Pflichtspalte nennt die Fehlermeldung die Spalte; es wird
  keine Ausgabedatei geschrieben.
- AC-3: Ein leerer Datensatz ergibt eine definierte leere Ausgabe ohne Ausnahme.

Technische Tasks beschreiben einen technischen Nutzen und objektive Nachweise.
Bugs brauchen beobachtetes und erwartetes Verhalten, Reproduktion und Regressionstest.
Die Given–When–Then-Struktur gehört nicht zum Standard.

## Priorisierung, Schätzung und Abhängigkeiten
- Ordne P0 (kritisch/blockierend), P1 (MVP notwendig), P2 (danach), P3 (optional)
  mit kurzer Begründung nach Nutzen, Risiko und Abhängigkeiten zu. P0 nur mit Evidenz.
- Ziehe riskante Annahmen bei hohem Schaden vor; nutze bei fehlender Evidenz einen
  zeitlich begrenzten technischen Untersuchungs-Task mit konkreter Entscheidungsfrage.
- Verwende grobe relative Größen XS/S/M/L mit Referenz-Story und Unsicherheit.
  Größe ist keine Stunden- oder Terminzusage. L-Einträge vor Umsetzung weiter schneiden.
- Referenziere Abhängigkeiten mit stabilen lokalen IDs oder existierenden Issues.
  Gib keine erfundenen GitHub-Nummern an. Prüfe Zyklen und blockierte MVP-Pfade.

## Definition of Ready und Definition of Done
DoR ist eine vereinbarte Arbeitshilfe, keine zusätzliche Scrum-Verpflichtung:
Ziel und Quelle klar, Scope begrenzt, Kriterien testbar, wesentliche Fragen geklärt,
Abhängigkeiten sichtbar, Größe einschätzbar und Umsetzung ausdrücklich freigegeben.
Kennzeichne fehlende Punkte; ein Entwurf darf noch nicht Ready sein.

DoD gilt gemeinsam: Kriterien nachgewiesen, angemessene Tests und Repository-
Qualitätsprüfungen bestanden, Review erledigt, Dokumentation aktuell, keine Secrets
oder unerklärten Änderungen. Projektspezifische Ergänzungen nur mit Quelle aufnehmen.
Ein Task-Abschluss oder bestandene CI allein beweist keine erfüllte Story.
