# Backlog und MVP-Roadmap: GlobalStockBot

Quelle: [Product Brief](product-brief.md), Repository-Stand `249f0cf` · Stand: 2026-10-31.
Prioritäten und Größen sind vorläufige Planung, keine Liefer- oder Sprintzusage.

## Quellen, Status und Auftragsgrenze

Der aktuelle Nutzerauftrag zur Zerlegung ist **Q-05**. Er bezeichnet den Product
Brief als freigegebene Produktgrundlage. Dessen ausdrücklich als Vorschlag,
Annahme oder offen markierte Details werden dadurch nicht pauschal bestätigt.
FR-01 bis FR-05 und NFR-01 bis NFR-04 bleiben die bestätigten Produktanforderungen;
die übrigen FR/NFR und PG-01 bleiben Vorschläge. IDs und Brief bleiben unverändert.

Q-05 erlaubt jetzt lokale Planung und PR-Vorbereitung und ersetzt insoweit die
historische Einschränkung „noch keine Epics/Stories“ des Discovery-Auftrags.
Er erlaubt weiterhin weder Issue-Veröffentlichung noch Anwendungscode,
Brokeranbindung, Orders oder neue Skills. Keiner der Entwürfe ist zur Umsetzung
freigegeben. Quellen Q-01 bis Q-04 behalten die Bedeutung aus dem Product Brief.

Zusätzliche Konkretisierungen aus Q-05 – konfigurierbare Strategien, explizite
Kauf-/Verkaufssignale, Nachvollziehbarkeit und spätere offizielle Broker-APIs –
werden über S-04, S-12 und T-09 als **Vorschläge** präzisiert. Sie passen zur Vision,
sind aber keine neue genehmigte Architektur. Der nun gewünschte MVP soll historische
Daten, mindestens eine Strategie, Backtesting, Risikoprüfung und Paper-Trading
abdecken; seine konkrete Markt-/Technik-/Zielwertausprägung bleibt Vorschlag.

## Story Map

| Nutzeraktivität | Schritte / Fähigkeiten | MVP-Schnitt | Spätere Optionen |
| --- | --- | --- | --- |
| Ziel und Daten klären | T-01, T-02, S-01, S-03, S-09 | Begrenztes Universum; rechtmäßige lokale Tagesdaten; Qualität und einfache Kapitalmaßnahmen | S-15: weiterer Markt, FX, Kalender |
| Strategie untersuchen | T-03, S-02, S-04, S-05 | Früher Referenzdurchlauf; eine konfigurierbare Regel; Kostenbacktest | S-14: zweite Strategie, weiterer Schnitt nötig |
| Portfolio kontrollieren | S-06, S-07, S-08 | Positionen/Cash, Pre-Trade-Limits und Pause | Weitere Risikoregeln nur nach neuem Refinement |
| Paper-Ablauf beobachten | T-04, T-05, S-10, S-11 | Lokaler Simulator, Journal und Wiederanlauf | T-09: offizieller API-Vergleich, noch kein Adapter |
| Ergebnis beurteilen und betreiben | S-12, T-06, S-13, T-07, T-08 | Berichte, lokaler Scheduler/Alarm, Restore und Abnahme | T-10: späterer Live-Freigabekatalog, keine Aktivierung |

Die Roadmap schneidet horizontal: Schon S-02 verbindet Eingabe, Signal, einfachen
Kapitalcheck, Simulation und Ergebnis. Spätere Schnitte härten denselben Ablauf.
Es entsteht keine monatelange reine Datenbank-/API-/UI-Schichtenfolge.

## Epics und optionale Features

| ID | Ebene | Ziel / Abschlussbedingung | Quelle / Status |
| --- | --- | --- | --- |
| [E-01](issues/E-01.md) | Epic | Verlässliche historische Aktienbasis; Historische Referenzdaten sind rechtmäßig nutzbar, geprüft und mit Split-/Dividendenfällen nachvollziehbar; unvollständige Daten werden nicht als vollständig ausgegeben. | FR-03; FR-07/FR-10 (Vorschlag); D-01 bis D-04; Zuschnitt Vorschlag |
| [E-02](issues/E-02.md) | Epic | Nachvollziehbare Strategieexperimente; Ein Referenzlauf und eine regelbasierte Strategie liefern deterministische Signale/Fills mit dokumentierter Zeit- und Kostenlogik. | FR-02/FR-03; FR-06/FR-08 (Vorschlag); NFR-02; Zuschnitt Vorschlag |
| [E-03](issues/E-03.md) | Epic | Kontrolliertes Portfolio und Risiko; Alle finalen Paper-Orderabsichten besitzen Risikobeschlüsse; Grenzfälle und Pausenregeln bestehen, Cash/Positionen sind korrekt. | FR-04; FR-11, NFR-06/NFR-11 (Vorschlag); D-09; Zuschnitt Vorschlag |
| [E-04](issues/E-04.md) | Epic | Lokales Paper-Trading ohne Echtgeldwirkung; Lokales Paper-Replay entspricht der historischen Referenz, erzeugt null externe Orders und übersteht definierte Unterbrechungen ohne Doppelbuchung. | FR-05, NFR-03; FR-09, NFR-08 (Vorschlag); Zuschnitt Vorschlag |
| [E-05](issues/E-05.md) | Epic | Überprüfbare Ergebnisse und begleiteter Betrieb; Freigegebene lokale Evaluationskriterien sind mit Berichten, Störungs-/Restore-Nachweisen und ehrlichen offenen Ergebnissen belegt. | FR-03 bis FR-05; FR-11/FR-12, NFR-05/NFR-09/NFR-10, PG-01 (Vorschlag); Zuschnitt Vorschlag |
| [E-06](issues/E-06.md) | Epic | Weitere Strategien und internationale Märkte; Separat geschnittene Folgeaufträge belegen eine zweite Strategie und einen zweiten Markt einschließlich Kalender/FX/Datenrechten. | FR-01/FR-02 bestätigt langfristig; konkrete Umsetzung Vorschlag; Zuschnitt Vorschlag |
| [E-07](issues/E-07.md) | Epic | Entscheidungsgrundlage für spätere Broker und Live-Freigabe; Belegter API-Vergleich und Freigabekatalog nennen offene Blocker; sie aktivieren keine Echtgeldfähigkeit. | NFR-02/FR-05; neue API-Ziele nur Vorschlag; D-01/D-03/D-08; Zuschnitt Vorschlag |

Die Epic-Dateien enthalten jeweils Nutzen, Scope, Nicht-Ziele, Abschlusskriterien
und Kinder. Eine zusätzliche Feature-Ebene bringt bei diesen begrenzten Gruppen
noch keinen Nutzen und wird nicht eingeführt. Fachliche Features sind etwa
qualifizierter Datenimport, Strategie-Replay, Risikofreigabe und Paper-Abgleich;
ihre implementierbaren Schnitte stehen direkt als Stories unter den Epics.

## Geordnete Einträge

Alle Links führen zu einzelnen Markdown-Bodys der vorhandenen Epic-/Story-/Task-
Vorlagen, ohne YAML-Metadaten. Jeder Entwurf ist **Vorschlag / nicht Ready**.
Alle angegebenen Abhängigkeiten sind fachliche Vorgänger, keine GitHub-Nummern.

| Rang | ID / Typ / Parent | Nutzenfähiger Schnitt | Quelle / Status | Priorität / Grund | Abhängigkeiten | Größe / Unsicherheit | DoR / offene Punkte | MVP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [T-01](issues/T-01.md) · Task · E-01 | MVP klären und Abnahmevertrag festhalten | FR-01, FR-03, FR-05; D-01, D-02, D-09, D-10; konkreter Schnitt Vorschlag | P1: Ohne Scope und Risikowerte wäre die nachfolgende Abnahme unklar. | keine | S / hoch | Nicht Ready: Freigabe / offene Scopefragen | MVP / Gate G0 |
| 2 | [T-02](issues/T-02.md) · Task · E-01 | Datenrechte und historisches Eingabeformat prüfen | FR-03; FR-07/FR-10 (Vorschlag); D-03, D-04; konkreter Schnitt Vorschlag | P1: Lizenz- und Qualitätsrisiken vor Datenintegration aufdecken. | T-01 | S / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / Gate G0 |
| 3 | [T-03](issues/T-03.md) · Task · E-02 | Minimale Kernverträge und Replay-Schnittstellen entscheiden | NFR-02; FR-06 (Vorschlag); D-04, D-05, D-06, D-07; konkreter Schnitt Vorschlag | P1: Kleine Verträge ermöglichen getrennte, testbare Entwicklungsaufträge. | T-01 | S / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / Gate G0 |
| 4 | [T-04](issues/T-04.md) · Task · E-04 | Offline-Ausführungsmodus gegen Live-Aufrufe absichern | FR-05, NFR-03; NFR-06/NFR-07 (Vorschlag); D-05; konkreter Schnitt Vorschlag | P1: Schutz vor externen Orders vor dem ersten ausführbaren Ablauf etablieren. | T-03 | S / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M1 |
| 5 | [S-01](issues/S-01.md) · Story · E-01 | Historische Tagesdaten aus einer lokalen Datei einlesen | FR-03; FR-10 (Vorschlag); D-02, D-03, D-04; konkreter Schnitt Vorschlag | P1: Erste nutzbare Datenbasis; Referenzgröße S. | T-02, T-03 | S / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M1 |
| 6 | [S-02](issues/S-02.md) · Story · E-02 | Ersten historischen Kauf-Verkauf-Ablauf durchspielen | FR-02, FR-03, FR-04, FR-05; FR-08/FR-11 (Vorschlag); konkreter Schnitt Vorschlag | P1: Frühester durchgängiger Nutzungsnachweis statt langer Infrastrukturphase. | T-04, S-01 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M1 |
| 7 | [S-03](issues/S-03.md) · Story · E-01 | Unvollständige und widersprüchliche Tagesdaten zurückweisen | FR-03; FR-07/FR-10, NFR-11 (Vorschlag); D-02, D-04; konkreter Schnitt Vorschlag | P1: Datenfehler verfälschen jede spätere Strategieauswertung. | S-01 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M2 |
| 8 | [S-04](issues/S-04.md) · Story · E-02 | Eine einfache Swing-Strategie konfigurieren und Signale berechnen | FR-02; FR-06 (Vorschlag); D-06; konkreter Schnitt Vorschlag | P1: Ersetzt feste Referenzsignale durch eine testbare Nutzerstrategie. | S-02 | S / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M2 |
| 9 | [S-05](issues/S-05.md) · Story · E-02 | Historische Mehrinstrument-Läufe mit Kosten auswerten | FR-02, FR-03; FR-08, NFR-05 (Vorschlag); D-06; konkreter Schnitt Vorschlag | P1: Macht aus dem Referenzlauf einen erklärbaren Backtest. | S-03, S-04 | M / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M2 |
| 10 | [S-06](issues/S-06.md) · Story · E-03 | Positionen und Cash nach simulierten Fills bewerten | FR-04; FR-11, NFR-11 (Vorschlag); D-05, D-09; konkreter Schnitt Vorschlag | P1: Verlässliche Bestände sind Grundlage aller Risikolimits. | S-05 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M2 |
| 11 | [S-07](issues/S-07.md) · Story · E-03 | Orderabsichten vor Ausführung gegen Kapital- und Positionslimits prüfen | FR-04, FR-05; NFR-06 (Vorschlag); D-09; konkreter Schnitt Vorschlag | P1: Risikoprüfung muss vor jedem allgemeinen Paper-Fill wirksam sein. | S-06, T-01 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M3 |
| 12 | [S-08](issues/S-08.md) · Story · E-03 | Verlustgrenzen und Pausenstatus durchsetzen | FR-04; FR-12, NFR-06 (Vorschlag); D-09; konkreter Schnitt Vorschlag | P1: Begrenzt Folgen fehlerhafter Daten oder Strategieausgaben. | S-07 | S / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M3 |
| 13 | [S-09](issues/S-09.md) · Story · E-01 | Splits und Dividenden in einer Referenzhistorie korrekt behandeln | FR-03, FR-04; FR-07 (Vorschlag); D-03, D-06; konkreter Schnitt Vorschlag | P1: Aktien-spezifische Fehler vor historischer Abnahme verhindern. | S-03, S-06 | M / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M3 |
| 14 | [T-05](issues/T-05.md) · Task · E-04 | Persistenzvertrag für das lokale Paper-Journal entscheiden | FR-04, FR-05; FR-09, NFR-08 (Vorschlag); D-07; konkreter Schnitt Vorschlag | P1: Verhindert Replay-Dopplungen vor länger laufender Simulation. | T-03 | S / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / vor M3 |
| 15 | [S-10](issues/S-10.md) · Story · E-04 | Lokale Paper-Sitzung schrittweise und persistent ausführen | FR-02, FR-04, FR-05; FR-06/FR-09 (Vorschlag); konkreter Schnitt Vorschlag | P1: Paper-End-to-End ohne Broker und ohne dauerhafte Internetabhängigkeit. | S-07, S-04, T-05 | M / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M3 |
| 16 | [S-11](issues/S-11.md) · Story · E-04 | Paper-Lauf nach Unterbrechung konsistent abgleichen | FR-04, FR-05; FR-09, NFR-08 (Vorschlag); konkreter Schnitt Vorschlag | P1: Wiederanlauf schützt langfristige Beobachtung vor stillen Bestandsfehlern. | S-10 | M / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M4 |
| 17 | [S-12](issues/S-12.md) · Story · E-05 | Backtest und Paper-Ergebnisse nachvollziehbar berichten | FR-03, FR-04; FR-11, NFR-05 (Vorschlag); konkreter Schnitt Vorschlag | P1: Nutzbarer Bericht macht die Evaluation überprüfbar. | S-06, S-09, S-11 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M4 |
| 18 | [T-06](issues/T-06.md) · Task · E-05 | Betriebs- und Evaluationsvertrag festlegen | FR-05; FR-12, NFR-09/NFR-10 (Vorschlag); D-08, D-10; konkreter Schnitt Vorschlag | P1: Zeit- und Betriebsziele sind bisher offen und dürfen nicht still bestätigt werden. | T-01 | S / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / vor M4 |
| 19 | [S-13](issues/S-13.md) · Story · E-05 | Lokale Paper-Läufe planen und Fehler sichtbar machen | FR-05; FR-12, NFR-06/NFR-10 (Vorschlag); konkreter Schnitt Vorschlag | P1: Kontrollierter Ablauf ist Voraussetzung für längerfristige Beobachtung. | T-06, S-11, S-08 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M4 |
| 20 | [T-07](issues/T-07.md) · Task · E-05 | Backup, Restore und Störungsnachweise für Paper-Betrieb erbringen | FR-05; NFR-08/NFR-10 (Vorschlag); konkreter Schnitt Vorschlag | P1: Nachweise vor längerem Beobachtungsfenster statt ungetesteter Wiederherstellung. | S-13, S-12, S-08 | M / mittel | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M4 |
| 21 | [T-08](issues/T-08.md) · Task · E-05 | Historische Evaluation und Paper-Abnahme dokumentieren | FR-02, FR-03, FR-04, FR-05, NFR-01/NFR-03; PG-01, NFR-09 (Vorschlag); konkreter Schnitt Vorschlag | P1: Abnahme verbindet Technik, Datenrechte und nachvollziehbare Nutzerergebnisse. | T-07, S-05, S-09, S-12 | M / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | MVP / M5 |
| 22 | [S-14](issues/S-14.md) · Story · E-06 | Zweite regelbasierte Strategie getrennt vergleichen | FR-02; FR-06/FR-11 (Vorschlag); D-06; konkreter Schnitt Vorschlag | P2: Mehrstrategiefähigkeit ist langfristig bestätigt, aber nicht für den ersten MVP nötig. | T-08 | L / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | Nach MVP |
| 23 | [S-15](issues/S-15.md) · Story · E-06 | Zusätzlichen Aktienmarkt mit Kalender und Währung auswerten | FR-01; FR-07, NFR-11 (Vorschlag); D-02, D-03; konkreter Schnitt Vorschlag | P2: Globale Abdeckung braucht nachgewiesene lokale Korrektheit als Basis. | T-08 | L / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | Nach MVP |
| 24 | [T-09](issues/T-09.md) · Task · E-07 | Offizielle Broker-Paper-APIs und Zulässigkeit vergleichen | NFR-02, FR-05; Product Brief D-01, D-03, D-08; neuer Planungsauftrag als Vorschlag; konkreter Schnitt Vorschlag | P2: Anbieterentscheidung erst nach belastbarem lokalen Ablauf, ohne jetzige Anbindung. | T-08 | S / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | Nach MVP / Untersuchung |
| 25 | [T-10](issues/T-10.md) · Task · E-07 | Freigabekriterien für möglichen Live-Handel untersuchen | FR-05, NFR-03; Product Brief R-05 bis R-09; neuer Planungsauftrag als Vorschlag; konkreter Schnitt Vorschlag | P3: Langfristiger Live-Wunsch bleibt hinter gesonderter Freigabe. | T-09 | S / hoch | Nicht Ready: Freigabe / Vorgänger / Detailentscheidungen | Nach MVP / nur Freigabekatalog |

## Gemeinsame Definitionen

**DoR – vorgeschlagene Arbeitshilfe:** Zielgruppe/Nutzen und Quellen sind klar;
Scope und Nicht-Ziele sind begrenzt; Kriterien sind nummeriert, testbar und
fehlerfallbezogen; wesentliche Entscheidungen sind tatsächlich geklärt;
Vorgänger und Eingabeverträge sind verfügbar; Größe ist einschätzbar; ein
konkreter Umsetzungsauftrag ist ausdrücklich freigegeben. Alle Entwürfe fehlen
mindestens beim letzten Punkt. Offene Entscheidungen bleiben Blocker, keine
stillschweigende Freigabe. Dokumentations-/Untersuchungstasks dürfen offene
Antworten als Ergebnis berichten; sie dürfen damit keine Implementierungsgates
als erfüllt markieren.

**DoD:** Jedes AC hat einen nachvollziehbaren Beleg; angemessene bestehende oder
neue Verhaltenstests sichern Erfolg und relevante Fehlerfälle. Python-Standards,
Ruff-Formatcheck/Lint, striktes mypy für src/scripts und pytest mit mindestens
85 % Coverage gelten gemäß Q-02. Bei Packaging-Änderungen gehört `uv build`
dazu. Tests dürfen nicht allein Implementierungsdetails spiegeln. Bei reinen
Untersuchungen sind Quellen, Entscheidungsstatus, Zeitbudget und Restfragen der
Nachweis. Dokumentation/angenommene ADRs sind aktuell; keine Secrets oder
unerklärten Änderungen; Review und explizite Abnahme des Outcomes fehlen nicht.
Ein grüner Task oder CI allein erfüllt keine übergeordnete Story oder ein Epic.

**Schätzreferenz:** S-01 = S (ein begrenztes lokales Datenformat inklusive
Fehlerfällen und Tests). XS wäre kleiner als S-01, S vergleichbar, M mehrere
eng zusammenhängende Regeln/Fehlerfälle, L zu groß oder zu unsicher für einen
Codex-Auftrag. E-01 bis E-07 sind L-Aggregate, S-14/S-15 müssen vor Umsetzung
weiter geschnitten werden. Größen sind relativ, keine Stunden, keine Velocity
und keine Schätzung der Wartezeit für eine 20-Sitzungen-Evaluation.
Untersuchungstasks haben zusätzlich ein vorgeschlagenes Zeitbudget und berichten
bei dessen Ablauf verbleibende Unsicherheit statt stillschweigend zu expandieren.

**INVEST-Prüfung:** Stories liefern beobachtbaren Nutzwert, bleiben verhandelbar
und enthalten eigene Referenz-/Fehlerfälle. Schnittstellen und Vorgänger sind
sichtbar; „Independent“ bedeutet hier keine Behauptung völliger Abhängigkeitsfreiheit.
S-02 reduziert den frühesten Durchlauf bewusst auf eine Handelsrunde; S-05,
S-06, S-07 und S-10 erweitern je eine fachliche Dimension. M-Stories enthalten
nur eng zusammengehörige Fälle; bei unerwarteter L-Komplexität erneut schneiden.
Spätere L-Platzhalter sind ausdrücklich nicht zur Umsetzung geeignet.

**Prioritäten:** P0 nur bei belegter aktueller Blockade mit kritischem Schaden;
eine solche Produktionsstörung liegt nicht vor. P1 trägt den vorgeschlagenen
MVP, P2 folgt danach, P3 ist optional/langfristig. Innerhalb P1 ordnen Schadensrisiko,
Lernwert und Abhängigkeiten die Arbeit. T-02/T-03 sind frühe Unsicherheitsreduktion;
T-04 schützt schon den ersten ausführbaren Ablauf. Kein Sprint oder Termin ist
zugesagt. Nach jedem vertikalen Schnitt Reihenfolge anhand neuer Evidenz prüfen.

## Anforderungsabdeckung

„Abgedeckt“ bedeutet **geplant**, nicht implementiert oder erfüllt. Konkrete
Kriterien und die vorgeschlagenen Zahlen stehen in den verlinkten Entwürfen.

| Brief-ID / Status | Geplante Entwürfe | MVP-Grenze / Nachweis |
| --- | --- | --- |
| FR-01 bestätigt langfristig | T-01, S-15 | Weltweit erst später; MVP begrenzt einen Markt. |
| FR-02 bestätigt langfristig | S-02, S-04, S-05, S-10, S-14 | Eine echte konfigurierbare Regel im MVP; mehrere Strategien später. |
| FR-03 bestätigt | T-02, S-01, S-03, S-05, S-09, T-08 | Historische Daten, Qualität und Kostenbacktest; nur synthetische Daten reichen nicht zur Marktabnahme. |
| FR-04 bestätigt | S-06, S-07, S-08, S-09, S-11 | Positions-/Cash-Korrektheit und freigegebene Risikoregeln. |
| FR-05 bestätigt | T-04, S-10, S-11, T-08, T-10 | Nur lokales Paper; Live separat und später. |
| FR-06 Vorschlag | T-03, S-04, S-10 | Referenzvergleich gemeinsamer Regeln. |
| FR-07 Vorschlag | T-02, S-03, S-09, S-15 | MVP begrenzte Identität/Kalender/Split/Dividende; komplexe Symbolwechsel und weitere Märkte später. |
| FR-08 Vorschlag | S-02, S-05 | Zeit-/Kostenmodell und handgerechnete Fills. |
| FR-09 Vorschlag | T-05, S-10, S-11 | Lokale Status-/Idempotenzfälle; keine Broker-Vertragstests. |
| FR-10 Vorschlag | S-01, S-03 | Unvollständige/fehlerhafte Daten sichtbar ablehnen. |
| FR-11 Vorschlag | S-06, S-12 | Bewertung und nachvollziehbarer Ergebnisbericht. |
| FR-12 Vorschlag | S-08, T-06, S-13 | Pause, lokaler Zeitplan und Alarmierung. |
| NFR-01 bestätigt | Gemeinsame DoD, jeder Implementierungseintrag, T-08 | Bestehende Python-Standards und Qualitätsschranken. |
| NFR-02 bestätigt | T-03, S-04, T-09 | Unabhängiger Kern; Anbieterfähigkeit erst später prüfen. |
| NFR-03 bestätigt | T-04, S-02, S-10, T-08 | Null Echtgeld-/Netzwerkorders im MVP. |
| NFR-04 bestätigt | Gemeinsame DoD und Veröffentlichungsstatus | Codex/GitHub-PR-Prozess; Projects nur spätere Planung, hier keine API-Einträge. |
| NFR-05 Vorschlag | S-05, S-10, S-12, T-08 | Zwei gleiche fachliche Ergebnisse bei festem Daten-/Versionsstand. |
| NFR-06 Vorschlag | T-04, S-07, S-08, S-13 | Fehler sperren neue simulierte Orders. |
| NFR-07 Vorschlag | T-04, S-13; später T-09 | Keine Secrets benötigt; keine Secret-Werte in Logs; Rotation erst bei späterem Credential-Bedarf. |
| NFR-08 Vorschlag | T-05, S-11, T-07 | Unterbrechung, Idempotenz und Restore. |
| NFR-09 Vorschlag | T-06, T-08 | Benchmark-Ziel 100 Instrumente/zehn Jahre/60 Sekunden erst nach Bestätigung. |
| NFR-10 Vorschlag | T-06, S-13, T-07 | 5-Minuten-Alarm, 4-Stunden-Restore, maximal ein Börsentag Verlust bleiben unbestätigte Ziele. |
| NFR-11 Vorschlag | T-03, S-03, S-06, S-15 | MVP eine Währung mit expliziter Zeit-/Rundungslogik, FX später. |
| PG-01 Vorschlag | T-01, T-06, T-08 | Freizugebende Abnahme statt Renditeziel; 20 Sitzungen nicht stillschweigend zugesagt. |

## Offene Entscheidungen und Risiken

D-IDs und R-/A-IDs beziehen sich auf den unveränderten Product Brief.

| Entscheidungen | Klärung / Entwürfe | Risiko / Verantwortungsrolle |
| --- | --- | --- |
| D-01, D-02, D-09, D-10 | T-01: Nutzerkreis, Jurisdiktion, Markt, Scope, Limits und Abnahme | R-05/R-06/R-08/R-10; Product Owner, konkrete Person offen. |
| D-03, D-04 | T-02: Rechte, Budget und Datenkonvention; S-01/S-03/S-09 | R-01/R-02/R-07/R-09, A-03; Product Owner mit Architekturberatung. |
| D-04, D-05, D-06 | T-03 und S-04: Kernverträge, Engine und einfache Strategie | R-01/R-03/R-10, A-02; Architekturrolle und Product Owner. |
| D-07 | T-05: Atomarität, IDs und Persistenz; S-10/S-11 | R-04; Architektur-/Betriebsrolle. |
| D-08, D-10 | T-06: Hostinggrenze, Zuständigkeit, Alarm und Evaluationsziele | R-04, A-01; Betriebsrolle mit Product Owner. |
| D-01, D-03, D-08 später | T-09/T-10: offizielle API-Rechte und möglicher Live-Freigabekatalog | R-03/R-05/R-07/R-08; Product Owner, qualifizierte externe Prüfung bei Bedarf. |

Keine Library, Datenbank, Broker oder Architekturvariante wird durch diese
Planung verbindlich gewählt. Modularer Monolith, typisierte Ports, pandas/Polars,
Parquet und SQLite/PostgreSQL bleiben Vergleichsoptionen. Technische Zeitbudgets
sind Vorschläge. Rechtliche Beratung, bezahlte Datenbeschaffung und laufende
Kosten wurden nicht beauftragt.

## Nicht-MVP und Veröffentlichungsstatus

S-14/S-15 und T-09/T-10 stehen außerhalb des MVP. Nicht vorgesehen sind jetzt
Live-Trading, echte Broker-Orders, Brokeranbindung, globale Märkte im ersten
Schnitt, Shortselling/Margin, ML-Optimierung, Webplattform oder Nutzung für Dritte.
Die nicht sicherheitsbedingten Produktausgrenzungen bleiben Scope-Vorschläge.

Alle **32 Dateien mit Issue-IDs** (7 Epics, 15 Stories, 10 Tasks) sind lokale
Entwürfe. Es gibt keine erfundenen GitHub-Nummern und keine veröffentlichten
Issues oder Projects-Einträge. Die vier vorhandenen Vorlagen Epic/Story/Task/Bug
wurden gelesen. Da aktuell kein reproduzierbarer offener Fehler nachgewiesen
ist, wird kein Bug erfunden. Bei einem tatsächlichen Defekt ist der Markdown-Body
von [bug.md](../../.github/ISSUE_TEMPLATE/bug.md) mit Reproduktion, Soll-/Ist,
Evidenz, Regressionstest und Planung zu verwenden; Veröffentlichung erfordert
weiterhin ausdrückliche Freigabe für die konkreten Einträge.

Auch die Genehmigung dieser Planung allein ist keine Umsetzungsfreigabe für
alle Issues. Bei später erlaubter Veröffentlichung bieten sich die Felder
Lokale ID, Epic, Priorität, MVP, Größe, Entscheidungsstatus und Abhängigkeiten
in GitHub Projects an; ein konkretes Board/Automationsschema ist noch offen.

PR-Basis: `feat/gbdj-product-discovery`, weil `main` bei Auftragsbeginn noch die
Factory enthielt. Der Planungsbranch ändert ausschließlich diese neuen
Planungsdateien. Nach Merge der Discovery kann der Planungs-PR auf `main`
umgestellt und sein Diff erneut geprüft werden. Kein automatischer Merge.

## Qualitätsprüfung dieser Planung

Prüfung am 2026-10-31:

| Prüffrage | Ergebnis / Nachweis |
| --- | --- |
| Bestätigte MVP-Anforderungen berücksichtigt? | FR-03 bis FR-05 und NFR-01 bis NFR-04 sind zugeordnet; FR-02 hat im MVP eine Strategie und später S-14 für mehrere. FR-01 bleibt bewusst langfristig. Die Matrix unterscheidet volle und begrenzte Abdeckung. |
| Epics fachlich sinnvoll und vollständig? | Sieben Outcomes mit Scope, Nicht-Zielen, Abschlusskriterien und eindeutig zugeordneten Kindern; keine separate Infrastruktur-/UI-Schichtenroadmap. |
| Stories für einzelne Codex-Aufträge begrenzt? | MVP-Stories S/M, konkret begrenzte Referenzfälle; L nur bei Epics und den explizit nicht Ready eingestuften späteren S-14/S-15. Unerwartete Vergrößerung erzwingt weiteres Refinement. |
| Kriterien objektiv prüfbar? | Nummerierte Referenz-, Grenz- und Fehlerfälle; Untersuchungen liefern belegte Entscheidungsvorlagen statt Implementierungsversprechen. Keine Given–When–Then-Struktur. |
| Abhängigkeiten und Blocker sichtbar? | Strukturprüfung für 25 Einzelaufträge: alle IDs auflösbar, keine Zyklen, Reihenfolge topologisch gültig. Fachliche Entscheidungsblocker sind zusätzlich genannt. |
| Doppelte oder überflüssige Einträge? | Jeder Einzelauftrag hat genau einen Epic-Parent. S-02 ist bewusst nur ein früher Referenzschnitt; S-05 erweitert Kosten/Universum, S-10 Persistenz/Sitzungen, S-11 Wiederanlauf. Kein paralleles zweites Handelssystem geplant. |
| Risiken und Freigaben sauber? | Datenrechte/Bias, Zeit-/Kostenmodell, Kapitalmaßnahmen, Doppelbuchung und versehentliche Echtgeldwirkung sind konkreten Einträgen zugeordnet. Sämtliche neuen Zuschnitte sind Vorschläge; keine Umsetzungsfreigaben behauptet. |
| MVP und spätere Erweiterungen getrennt? | 21 Einzelaufträge MVP, vier danach; S-14/S-15 und T-09/T-10 ausdrücklich außerhalb des MVP. Keine Brokeranbindung. |

Technisch geprüft: **32 einzelne Issue-Dateien** mit passenden Überschriften aus
den bestehenden Epic-/Story-/Task-Vorlagen, ohne YAML-Metadaten; gültige lokale
Links und Anker, eindeutige IDs/Parents und Verweise auf alle FR-/NFR-IDs.

Repository-Prüfungen: Ruff-Formatcheck (30 Dateien), Ruff-Lint und mypy für
src/scripts bestanden. pytest: **48 bestanden, null fehlgeschlagen/übersprungen,
96,15 % Coverage** bei 85 % Untergrenze, Python 3.12.15. `git diff --check`
bestand. Paketbau wurde für diesen reinen Dokumentationsdiff nicht erneut
ausgeführt; Paketierung und Dependencies bleiben unverändert. Es wurden keine
neuen Tests zur bloßen Spiegelung der Markdown-Dateien hinzugefügt.

Diese Prüfungen validieren Planung und bestehende Projektbasis. Sie belegen
keine implementierten Handelsfunktionen, Marktdatenqualität eines Anbieters,
Brokerkompatibilität oder bestandene MVP-Evaluation. Kein Backtest/Paper-Lauf
wurde ausgeführt; sämtliche AC-Checkboxen der geplanten Issues bleiben offen.
