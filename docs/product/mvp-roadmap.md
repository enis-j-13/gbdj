# MVP-Roadmap: GlobalStockBot

Quelle: [Product Brief](product-brief.md), Stand `249f0cf`, und
[Backlog](backlog.md) · 2026-10-31 · **Vorschlag, keine Lieferzusage**.
IDs verweisen auf lokale Entwürfe; keine GitHub-Issues werden veröffentlicht.

## MVP und begründete Abgrenzung

Ein begrenztes Aktienuniversum, eine Währung, ungehebelte Long-Positionen,
Tagesdaten und eine transparente Swing-Regel ermöglichen einen nachvollziehbaren
historischen Ablauf bis zur lokalen Paper-Simulation. US-Aktien/USD und eine
SMA-Kreuzung sind Empfehlungen, keine bestätigten Entscheidungen. Kapital,
Limits, Kalender, Rechte, Strategie und Abnahmewerte werden zuerst geklärt.
Swing beschreibt den Produkthorizont; eine Regel garantiert keine fixe Haltedauer.

Der MVP umfasst historische Daten mit nachgewiesenen Rechten, mindestens eine
konfigurierbare Regel, Kostenbacktesting, Positionsführung, Pre-Trade-Risiko,
Pause, lokales persistentes Paper-Trading und nachvollziehbare Ergebnisse.
Synthetische Daten erlauben frühe Techniknachweise, ersetzen aber keine
historische Marktevaluation. Ein lokaler Simulator benötigt keine Broker-API.
Neue Tagesdaten werden für den späteren lokalen Beobachtungslauf als geprüfte
Dateien bereitgestellt; Datenbeschaffung/Hosting sind keine implizite Zusatzleistung.

Keine echten Broker-Orders, keine Brokerintegration und kein Live-Code gehören
zum MVP. Ein Simulator prüft keine Brokerfähigkeit und reale Paper-Fills.
Globale Märkte, FX, mehrere produktive Strategien, Shortselling, Margin und
kommerzielle Nutzung würden den ersten Schnitt durch weitere Rechte-, Daten-
und Betriebsfragen überladen; sie werden separat verfeinert. Freqtrade ist ein
funktionales Vorbild, keine beschlossene technische Basis.

## MVP-Abfolge

Die Reihenfolge im Backlog ist topologisch gültig. Unabhängige Dokumentations-
oder Untersuchungsaufgaben dürfen nach ihren tatsächlichen Vorgängern vorgezogen
werden; daraus wird kein zusätzlicher Auftrag abgeleitet. Es gibt keine
Sprint- oder Kalendertermine und keine zugesagte Teamkapazität.

| Schritt | Stories / Tasks | Nutzbarer Zwischenstand / Lernziel | Abhängigkeiten / Risiko | Abschlussnachweis |
| --- | --- | --- | --- | --- |
| G0 – Entscheidungen vorbereiten | [T-01](issues/T-01.md), [T-02](issues/T-02.md), [T-03](issues/T-03.md) | Begrenzte Daten-/Scope-/Kernverträge statt unbemerkter Annahmen | T-02/T-03 nach T-01; Rechte, Kalender, Zeit-/Kostenmodell offen | Dokumentierte tatsächliche Entscheidungen und verbleibende Blocker; keine erfundene Freigabe. |
| M1 – erster vollständiger Technikpfad | [T-04](issues/T-04.md), [S-01](issues/S-01.md), [S-02](issues/S-02.md) | Lokale Kurse → feste Referenzsignale → eine simulierte Handelsrunde → Cash/Ergebnis | T-04/S-01 nach G0; S-02 nach beiden. Nur minimaler Kapitalcheck, noch keine allgemeine Risikoevaluation | Handgerechneter Offline-Lauf, keine externen Aufrufe, identische Wiederholung. |
| M2 – historische Strategieauswertung | [S-03](issues/S-03.md), [S-04](issues/S-04.md), [S-05](issues/S-05.md), [S-06](issues/S-06.md) | Qualitätsgeprüfte Daten, eine konfigurierbare Regel, Kosten, Positionen und Bewertung | Qualitätsfehler und Look-ahead vor Ergebnisauswertung erkennen | Referenzsignale/-fills, deterministische Mehrinstrument-Auswertung, handgerechnete Bestände. Noch keine abgeschlossene Marktabnahme. |
| M3 – kontrolliertes lokales Paper-Trading | [S-07](issues/S-07.md), [S-08](issues/S-08.md), [S-09](issues/S-09.md), [T-05](issues/T-05.md), [S-10](issues/S-10.md) | Pre-Trade-Limits, Pause, Kapitalmaßnahmen und persistente Sitzungsschritte | T-05 kann nach T-03 vorgezogen werden; S-10 benötigt S-07/S-04/T-05. Limits und Persistenzentscheidung bestätigen | Split-/Dividendenreferenz, Limitgrenzen, gleiche Regeln im Backtest und lokalen Paper-Replay. |
| M4 – beobachtbarer und wiederherstellbarer Ablauf | [S-11](issues/S-11.md), [S-12](issues/S-12.md), [T-06](issues/T-06.md), [S-13](issues/S-13.md), [T-07](issues/T-07.md) | Abgleich, Bericht, geplante lokale Läufe und Restore | T-06 kann nach T-01 vorgezogen werden; S-13 benötigt auch S-08. Alarm-/Betriebsziele offen | Zehn definierte Abbrüche, keine Doppelbuchungen, gemessene Alarme, Restore in leeres Ziel. |
| M5 – historische und Paper-Evaluation | [T-08](issues/T-08.md) | Belegte Abnahme mit ehrlichen Grenzen | Vorherige Kette, freigegebene Datenrechte, bestätigte Zielwerte und Referenzhardware | Historischer Referenzbericht, Reproduzierbarkeit, Risiko-/Sicherheitsbelege und bestätigtes Beobachtungsfenster. |

**Gates:** M1 ist nur ein früher Techniknachweis. Erst M3 besitzt die vollständigen
geplanten Risiko-/Kapitalmaßnahmenfunktionen; erst M5 kann als MVP-Evaluation
abgenommen werden. Offene D-Entscheidungen bleiben an den jeweils betroffenen
Issues blockierend. Kostenpflichtige Daten oder unzureichende Rechte dürfen nicht
mit einer rein synthetischen „Marktabnahme“ umgangen werden.

Die 20 Börsensitzungen aus PG-01 und Performance-/Alarm-/Restorezahlen bleiben
Vorschläge. T-01/T-06 müssen diese bestätigen oder eine ausdrückliche Änderung
festhalten. Beschleunigtes Replay beweist keinen 20-tägigen Betrieb; Beobachtungszeit
ist von Implementierungsaufwand zu unterscheiden. Rendite ist kein Abnahmekriterium.

## Erste fünf empfohlene Entwicklungs-Issues

Diese Reihenfolge ist eine Empfehlung für spätere Einzelaufträge, keine aktuelle
Implementierungsfreigabe. Die ersten drei sind begrenzte Klärungs-/Entscheidungstasks.

1. **T-01:** Scope und Abnahmevertrag – legt Markt, Grenzen, Kapital und offene Nutzerfragen offen.
2. **T-02:** Datenrechte und Eingabeformat – reduziert Lizenz-/Qualitätsrisiken vor Datenverwendung.
3. **T-03:** Kernverträge und Replay-Semantik – entscheidet die kleinsten nötigen, brokerunabhängigen Grenzen.
4. **T-04:** Offline-Modus absichern – verhindert externe Orderwirkung vor ausführbaren Pfaden.
5. **S-01:** Lokale historische Datei importieren – liefert den ersten nutzbaren Entwicklungsbaustein.

Danach liefert S-02 den ersten End-to-End-Erfolg. T-02 und T-03 sind nach T-01
fachlich unabhängig; ihre Ergebnisse werden vor Umsetzung von S-01 abgestimmt.

## Nach dem MVP

- **S-14 / E-06:** Zweite Strategie, zunächst kleiner schneiden und Regeln bestätigen.
- **S-15 / E-06:** Zweiter Aktienmarkt, zunächst Identität, Kalender, Datenrechte und FX separat verfeinern.
- **T-09 / E-07:** Offizielle Broker-Paper-APIs vergleichen, keine Verbindung herstellen.
- **T-10 / E-07:** Spätere Live-Freigabekriterien untersuchen, keine Freigabe erteilen.

## Laufendes Refinement und Freigaben

Nach jedem Zwischenstand Referenzfälle, Datenqualität, neue Risiken und Größe
prüfen. Nicht erfüllte ACs bleiben sichtbar; Scope-Änderungen erfordern eine
explizite Entscheidung. L-Einträge werden vor Implementierung geteilt. Die
[Anforderungsmatrix und gemeinsamen Definitionen](backlog.md) gelten für alle
Einträge. Ein genehmigter Plan oder ein veröffentlichter Eintrag allein ist
weder Auftrag zur Umsetzung noch Live-Freigabe.
