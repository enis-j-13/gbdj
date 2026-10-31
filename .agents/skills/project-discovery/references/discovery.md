# Methode und Qualitätskriterien

## Produktverständnis
- Vision: Welchen dauerhaften Nutzen soll das Produkt für welche Zielgruppe schaffen?
- Product Goal: Welches überprüfbare Ergebnis soll bis zu welchem Zeitpunkt
  erreicht sein? Metrik, Zielwert und Messweg angeben; Unbekanntes kennzeichnen.
- Problem zuerst beschreiben; vorgeschlagene technische Lösungen getrennt halten.

## Anforderungen und Status
Jede Anforderung erhält ID, Status, Beschreibung, Quelle und Prüfmethode.
Funktionale Anforderungen beschreiben beobachtbare Fähigkeiten. Nichtfunktionale
Anforderungen beschreiben z. B. Sicherheit, Zuverlässigkeit, Performance,
Zugänglichkeit oder Betrieb mit Kontext und messbaren Grenzen.

| Status | Bedeutung |
| --- | --- |
| Bestätigt | Expliziter Nutzerauftrag oder referenzierte bestehende Vereinbarung |
| Vorschlag | Fachliche Empfehlung, die noch nicht beauftragt wurde |
| Annahme | Vorläufige Arbeitsgrundlage mit Risiko und Validierungsweg |
| Offen | Entscheidung oder Information fehlt; Auswirkung dokumentieren |

Beispiel: `NFR-01 · Vorschlag · Eine lokale Auswertung von 10.000 Datensätzen
benötigt auf vereinbarter Referenzhardware höchstens 2 Sekunden. Messung über
Benchmark mit festgelegtem Datensatz.` Zahlen gelten erst nach Bestätigung.

## MVP und Unsicherheit
- MVP als kleinsten durchgängigen Nutzungsablauf mit Lernziel beschreiben.
- Anforderungen über IDs zuordnen; optionale Wünsche und Nicht-Ziele explizit trennen.
- Risiken mit Auswirkung, Eintrittswahrscheinlichkeit, Gegenmaßnahme und Auslöser
  festhalten. Keine scheinpräzisen Bewertungen ohne Daten.
- Annahmen erhalten einen Prüfweg; offene Entscheidungen eine verantwortliche
  Rolle und benötigte Evidenz, soweit bekannt. Unbekannte Rollen nicht erfinden.
- Konflikte zwischen Ziel, Scope, Budget und Qualitätsanforderungen offen benennen.
