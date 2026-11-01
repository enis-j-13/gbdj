# Product Brief: GlobalStockBot (GBDJ)

Stand: 2026-10-31 · Entscheidungsstatus: Entwurf; nur als **Bestätigt** markierte
Aussagen sind durch die unten genannten Quellen belegt. Dieser Brief ist eine
Entscheidungsgrundlage und keine Freigabe zur Umsetzung des vorgeschlagenen MVP.
Er folgt der bestehenden Discovery-Methode und Product-Brief-Vorlage.

## Ausgangslage und Zielgruppe

Der Nutzer möchte eine professionelle Python-Plattform nach dem funktionalen
Vorbild von Freqtrade für Aktien entwickeln. Langfristig sollen verschiedene
internationale Börsen und mehrere regelbasierte Strategien unterstützt werden.
Swing-Trading bedeutet hier Haltedauern von mehreren Tagen bis Wochen.

**Annahme A-01:** Erste Zielgruppe sind technisch versierte private Anleger,
die eigene Swing-Strategien systematisch untersuchen und im Paper-Betrieb
beobachten möchten. Heutiger Ablauf, konkrete Anwenderprobleme, Vorerfahrung,
Nutzung für Dritte und Jurisdiktion sind noch nicht erhoben. Die Problemhypothese
lautet: Historische Analyse, Risikoregeln und simulierte Ausführung sind oft
getrennt; dadurch entstehen schwer vergleichbare Ergebnisse und unbemerkte
Abweichungen zwischen Strategieabsicht und Portfoliozustand. Diese Hypothese
muss anhand eines realen Arbeitsablaufs validiert werden.

### Quellen und Status

- **Q-01:** Nutzerauftrag „GBDJ initialisieren und Product Discovery durchführen“
  vom 2026-10-31: Projektidee, bestätigte Anforderungen, Umfang und Einschränkungen.
- **Q-02:** [AGENTS.md](../../AGENTS.md), [Python-Standards](../standards/python.md),
  [Teststandards](../standards/testing.md) und bestehender
  [Toolchain-ADR](../architecture/decisions/0001-python-toolchain.md).
- **Q-03:** Fachliche Empfehlungen dieses Discovery-Entwurfs; noch keine Zustimmung.
- **Q-04:** Offizielle Anbieterquellen im Abschnitt „Daten und Broker“;
  aktuelle Inhalte konnten wegen HTTP-403-Netzwerksperren nicht abgerufen werden.
  Sie sind Prüfziele, kein Nachweis aktueller Preise, Marktdeckung oder Rechte.

**Bestätigt** = expliziter Auftrag/bestehende Vereinbarung; **Vorschlag** = Empfehlung;
**Annahme** = vorläufige Grundlage mit Prüfweg; **Offen** = fehlende Entscheidung.
Eine bestätigte langfristige Fähigkeit ist keine automatische Zusage für den MVP.

## Product Vision

**Aus Q-01 abgeleitete Formulierung:** GlobalStockBot soll regelbasiertes
Swing-Trading in internationalen Aktienmärkten nachvollziehbar und erweiterbar
machen: vom reproduzierbaren historischen Experiment über kontrolliertes
Paper-Trading bis zu einer später separat freizugebenden automatisierten
Live-Ausführung. Nutzer sollen Strategie-, Daten- und Risikoeffekte verstehen
können. Das Produkt verspricht weder Gewinne noch die Übertragbarkeit simulierter
Ergebnisse auf den Echtgeldhandel. Die konkrete Visionsformulierung ist ein Vorschlag.

## Product Goal

**Vorschlag PG-01:** Zum Ende einer noch zu terminierenden MVP-Evaluation kann
ein Nutzer einen vollständigen Ablauf für ein vereinbartes Aktienuniversum
reproduzieren: geprüfte Tagesdaten → historische Strategieauswertung →
Risikoprüfung → Paper-Ausführung → Abgleich und Bericht.

Vorgeschlagene Messung auf einem versionierten Referenzdatensatz und dokumentierter
Hardware: zwei Wiederholungen liefern identische Signale und Portfoliobuchungen;
alle erzeugten Orders besitzen ein Risikoprüfergebnis; kein Echtgeld-Endpunkt
wird angesprochen. Eine anschließende Beobachtung über 20 Börsensitzungen soll
null ungeklärte doppelte Orders und null ungeklärte Bestandsdifferenzen aufweisen.
Zielwerte, Benchmark und Zeitraum sind noch zu bestätigen (D-02, D-10).
Rendite ist kein Abnahmekriterium. Termin, Budget und verfügbare Entwicklungszeit
sind offen; 20 Sitzungen allein belegen keine Strategieprofitabilität.

## Funktionale Anforderungen

| ID | Status | Fähigkeit | Quelle | Prüfmethode |
| --- | --- | --- | --- | --- |
| FR-01 | Bestätigt | Langfristig Aktien verschiedener internationaler Börsen verarbeiten und handeln können. | Q-01 | Spätere marktbezogene Vertragstests für Instrumente, Währungen, Kalender und Ausführung; erster Markt offen. |
| FR-02 | Bestätigt | Mehrere regelbasierte Swing-Strategien mit Haltedauern von Tagen bis Wochen unterstützen. | Q-01 | Versionierte Strategien auf Referenzdaten; Regeln und resultierende Signale nachvollziehen. |
| FR-03 | Bestätigt | Historische Marktdaten für Analysen und Backtests verwenden. | Q-01 | Datenimport und historischer Lauf mit belegter Datenherkunft und erwarteten Ergebnissen. |
| FR-04 | Bestätigt | Portfolio- und Risikomanagement bereitstellen. | Q-01 | Gezielte Tests für freigegebene Risikoregeln und Portfolioabgleich; konkrete Limits offen. |
| FR-05 | Bestätigt | Zunächst ausschließlich Paper-Trading; vollautomatischer Live-Handel erst nach ausdrücklicher Freigabe. | Q-01 | Betriebsmodus und Ausführungsziel prüfen; Tests erzwingen Ablehnung von Echtgeld-Orders. |
| FR-06 | Vorschlag | Backtest und Paper-Betrieb verwenden dieselben versionierten Signal- und Risikoregeln. | Q-03 | Gemeinsamen Referenzfall durch beide Abläufe abspielen und Signale vergleichen. |
| FR-07 | Vorschlag | Instrumente börsen-, währungs- und zeitraumbezogen identifizieren; Symbolwechsel, Splits, Dividenden und Delistings nachvollziehen. | Q-03 | Referenzfälle für Corporate Actions, identische Ticker an verschiedenen Börsen und historische Symbolzuordnung. |
| FR-08 | Vorschlag | Backtests berücksichtigen Gebühren, Spread, Slippage, Handelskalender und den frühesten zulässigen Ausführungszeitpunkt. | Q-03 | Handgerechnete Beispiele einschließlich Signal am Schlusskurs und Ausführung frühestens in der Folgesitzung. |
| FR-09 | Vorschlag | Orders, Teilfüllungen, Ablehnungen und Stornierungen nachvollziehen; Wiederholungen idempotent behandeln und Bestände abgleichen. | Q-03 | Simulierte Zeitüberschreitungen, doppelte Ereignisse und Neustarts ohne Doppelbuchung. |
| FR-10 | Vorschlag | Datenqualität vor einer Auswertung prüfen und fehlende, veraltete oder widersprüchliche Daten sichtbar ablehnen. | Q-03 | Fehlerdatensätze mit Lücken, Duplikaten, falschen Zeitstempeln und ungültigen OHLC-Werten. |
| FR-11 | Vorschlag | Berichte zu Positionen, Cash, Exposure, Drawdown und Performance einschließlich Kosten erstellen. | Q-03 | Gegen handgerechnetes Portfolio prüfen; Währung und Bewertungszeitpunkt ausweisen. |
| FR-12 | Vorschlag | Geplante Läufe, Statusmeldungen, Alarmierung und kontrolliertes Pausieren ermöglichen. | Q-03 | Ausfall- und Wiederanlauftest mit dokumentiertem Zustand und Alarm. |

## Nichtfunktionale Anforderungen

| ID | Status | Qualitätsziel und Kontext | Quelle | Messung und Grenze |
| --- | --- | --- | --- | --- |
| NFR-01 | Bestätigt | Python als primäre Sprache; bestehende Factory-Standards und Python 3.12 als Startversion einhalten. | Q-01, Q-02 | Ruff, striktes mypy, pytest mit mindestens 85 % Coverage und Paketbau gemäß Repository-Vorgaben. |
| NFR-02 | Bestätigt | Brokerunabhängige Architektur. | Q-01 | Kernregeln dürfen keine anbieterspezifischen SDK-Typen benötigen; später gemeinsamer Adapter-Vertrag mit Test-Doubles. Konkretes Design offen. |
| NFR-03 | Bestätigt | Keine Echtgeld-Orders während Entwicklung und Tests. | Q-01 | Null Requests an Live-Order-Endpunkte; spätere Negativtests für Modus, Ziel und Credentials. Aktuell keine Brokerintegration vorhanden. |
| NFR-04 | Bestätigt | Entwicklung mit Codex Cloud, GitHub und GitHub Projects unter bestehenden Standards. | Q-01, Q-02 | Reproduzierbarer Setup- und PR-/CI-Ablauf; Projects wird erst in später beauftragter Planung genutzt, hier keine Einträge. |
| NFR-05 | Vorschlag | Historische Ergebnisse sind reproduzierbar und auditierbar. | Q-03 | Zwei Läufe bei gleichen Daten, Versionen, Konfiguration und Seed ergeben identische Signale/Buchungen; Run-ID und Hashes sind vorhanden. |
| NFR-06 | Vorschlag | Fehler führen zum sicheren Stillstand neuer Orders. | Q-03 | Bei veralteten Daten, fehlgeschlagenem Abgleich, unbekanntem Orderstatus oder Limitverletzung entstehen null neue Orders bis zur Klärung. |
| NFR-07 | Vorschlag | Zugangsdaten sind isoliert und werden nicht protokolliert. | Q-02, Q-03 | Keine Secrets in Git oder Logs; ausschließlich getrennte Paper-Credentials, minimale Rechte und dokumentierte Rotation vor späterer Integration. |
| NFR-08 | Vorschlag | Wiederanlauf erhält Konsistenz. | Q-03 | Unterbrochenen Paper-Lauf zehnmal an definierten Stellen neu starten: null doppelte Buchungen, null ungeklärte Bestandsdifferenzen. |
| NFR-09 | Vorschlag | Tagesdatenverarbeitung erfüllt ein vereinbartes Laufzeitbudget. | Q-03 | Benchmark: 100 Instrumente, zehn Jahre Tagesdaten, eine Strategie in höchstens 60 Sekunden auf noch festzulegender Hardware; Beschaffungszeit separat messen. |
| NFR-10 | Vorschlag | Betrieb ist beobachtbar und wiederherstellbar. | Q-03 | Fehleralarm innerhalb von fünf Minuten; Wiederherstellung innerhalb von vier Stunden bei maximal einem Börsentag Datenverlust; Restore-Test vor Evaluation. Zuständigkeit und Bereitschaft offen. |
| NFR-11 | Vorschlag | Zeit-, Währungs- und Datenmodell ist explizit. | Q-03 | UTC für Ereignisse plus Börsenzeitzone/Handelstag; keine implizite Währungsvermischung; Kalender-, DST- und Geldrundungsfälle müssen bestehen. |

## MVP und Nicht-Ziele

**Der gesamte konkrete MVP-Zuschnitt ist ein Vorschlag.** Lernziel ist die
technische und fachliche Konsistenz des vollständigen Paper-Ablaufs, nicht das
Erreichen einer Rendite.

Vorgeschlagener kleinster Ablauf: feste Liste liquider US-Aktien, USD als einzige
Bewertungswährung, Long-only, ungehebelt, Tagesdaten und Auswertung nach offiziellem
Handelsschluss. Eine transparente, noch auszuwählende Referenzstrategie erzeugt
Signale für frühestens die nächste reguläre Sitzung. Auf qualitätsgeprüften Daten
werden Kosten und Ausführungsannahmen simuliert; danach folgt eine Paper-Beobachtung
mit einem noch auszuwählenden Anbieter oder zunächst einem lokalen Simulator.
Ein lokaler Simulator allein bestätigt keine externe Brokerkompatibilität.
Risikoregeln werden vor jeder simulierten Order ausgewertet; Bericht und Abgleich
schließen den Ablauf ab. Ein zweiter Strategie-Test-Double kann Erweiterbarkeit
prüfen, ohne mehrere produktive Strategien in den MVP aufzunehmen.

- **Enthaltene Anforderungen:** FR-02 bis FR-05 in diesem begrenzten Umfang,
  FR-06 bis FR-12 als Vorschläge; NFR-01 bis NFR-04 als Vorgaben und
  NFR-05 bis NFR-11 als vorgeschlagene Qualitätsziele. FR-01 ist langfristig;
  der MVP demonstriert noch keine globale Marktabdeckung.
- **Vorgeschlagene Abnahme:** PG-01, dokumentierte Datenlizenz, freigegebene
  Risikolimits, deterministische Referenzfälle und nachvollziehbare Paper-Berichte.
- **Nicht-Ziele des vorgeschlagenen MVP:** Echtgeldhandel, globale Börsenabdeckung,
  Shortselling, Margin, Derivate, Intraday-/Hochfrequenzhandel, ML-Optimierung,
  automatische Parametersuche, Multi-Tenancy, öffentliche Weboberfläche und
  kommerzieller Betrieb für Dritte. Diese Grenzen außer Echtgeldhandel sind
  unbestätigte Scope-Empfehlungen, keine dauerhaften Produktausschlüsse.
- **Grenzen dieses Auftrags (bestätigt):** Nur Bootstrap, README und Product Brief.
  Keine Epics, Stories, Issues, Projects-Einträge, Trading-Implementierung,
  Brokeranbindung, Live-Orders oder neuen Skills; PR ohne automatischen Merge.

## Daten und Broker: Optionen zur Prüfung

Alle folgenden Kandidaten und Technologiezuordnungen sind **Vorschläge (Q-03)**.
Offizielle Einstiegslinks (Q-04) müssen vor einer Auswahl inhaltlich und anhand
konkreter Tarife, Konten und Jurisdiktionen überprüft werden. Abrufversuche am
2026-10-31 endeten mit HTTP 403 am Netzwerkproxy; es wurden keine Accounts oder
Verbindungen eingerichtet. Preise, Zulässigkeit und aktuelle Verfügbarkeit sind
nicht bestätigt.

| Bereich | Kandidat / offizielle Quelle | Eignungshypothese | Noch zu prüfen |
| --- | --- | --- | --- |
| Paper-Broker für begrenzten Einstieg | [Alpaca Paper Trading](https://docs.alpaca.markets/docs/paper-trading) | Prüfkandidat für US-Aktien und getrennten Paper-Betrieb. | Wohnsitz/Kontozulassung, API-Limits, Paper-vs-Live-Unterschiede, Datenfeed und Marktabdeckung. |
| Internationaler Broker | [Interactive Brokers TWS API](https://www.interactivebrokers.com/campus/ibkr-api-page/twsapi-doc/) | Prüfkandidat für langfristige internationale Abdeckung. | Börsen-/Produktberechtigungen, Paper-Konto, TWS-/Gateway-Betrieb, Sitzungsneustarts, Datenabonnements und Hostingbedingungen. |
| Historische Daten | [Alpha Vantage Dokumentation](https://www.alphavantage.co/documentation/) | Kandidat für historische Aktienzeitreihen; alternativ separat lizenzierte Brokerdaten evaluieren. | Börsenabdeckung, Historientiefe, Adjustierungen, Delistings, Limits, Kosten und Nutzungsrechte pro Tarif. |
| Börsendatenrechte | [NYSE Pricing & Policies](https://www.nyse.com/market-data/pricing-policies) | Beispiel für separat zu prüfende Börsendatenbedingungen. | Interne/automatisierte Nutzung, Speicherung, Weitergabe, professionelle Einstufung; andere Börsen separat prüfen. |

Datenqualität entscheidet über die Aussagekraft: konsolidierter oder einzelner
Handelsplatz, verzögert oder Echtzeit, OHLCV-Definition, Handelskalender,
Zeitzonen, Corporate Actions, ausgefallene Sitzungen und historische
Index-/Universumszusammensetzung müssen dokumentiert sein. Für Backtests sind
Point-in-Time-Universen einschließlich ausgeschiedener Aktien nötig, um
Survivorship Bias sichtbar zu vermeiden. Bereinigte Preise müssen zur
Dividenden-/Cash-Buchhaltung passen; keine doppelte Ertragszählung.

**Vorschlag:** Rohdaten unverändert mit Herkunft, Abrufzeit, Lizenzversion und Hash
aufbewahren; normalisierte Daten versionieren. Signal- und Ausführungspreise
explizit trennen. Bei fehlenden Rechten oder unzureichender Historie den Testumfang
einschränken und kennzeichnen, statt den Datensatz als vollständig zu behandeln.
Kostenpflichtige Beschaffung ist nicht autorisiert; Budget und Rechte sind D-03.

## Architektur und Erweiterbarkeit

**Vorschlag:** Ein modularer Monolith mit klaren Grenzen bietet einen kleinen
Betriebsumfang. Denkbare Module sind Instrumente/Kalender, Marktdaten,
Strategien, Backtesting, Portfolio/Risiko, Ausführung sowie Reporting/Betrieb.
Ports und Adapter können Datenanbieter, Persistenz und Broker kapseln.
Ein Domänenmodell für Signal, Orderabsicht, Risikobeschluss, Orderstatus und
Fill trennt Entscheidungen von externer I/O. Brokerunabhängigkeit bedeutet
keine identischen Fähigkeiten aller Anbieter: Capability-Prüfungen sollen
nicht unterstützte Ordertypen ablehnen und Unterschiede sichtbar machen.

| Technologieoption | Nutzen / Abwägung | Status |
| --- | --- | --- |
| Python 3.12, uv, pytest, Ruff, mypy | Bestehende Factory-Toolchain weiterverwenden. | Bestätigt durch Q-02; keine neue Architekturentscheidung. |
| `typing.Protocol`, Dataclasses, explizite Geld-/Rundungsregeln | Kleine typisierte Schnittstellen ohne frühe Framework-Abhängigkeit. | Vorschlag; D-05. |
| pandas oder Polars; Parquet über PyArrow | Tabellarische Analyse und reproduzierbare Datenstände; Ergonomie gegen Ressourcenbedarf benchmarken. | Vorschlag; D-04. |
| Eigener kleiner ereignisbasierter Backtest oder bestehende Engine | Kontrolle über Corporate Actions und Ausführung gegen Wartungsaufwand; bestehende Engine anhand Lizenz und fachlicher Semantik prüfen. | Offen; D-06. |
| SQLite für lokale Metadaten, später eventuell PostgreSQL | Wenig Betriebsaufwand gegen konkurrierende Schreibzugriffe; Migration nicht vorwegnehmen. | Vorschlag; D-07. |
| CLI und einzelner geplanter Worker | Nachvollziehbare Läufe ohne Webplattform; Scheduler, Persistenz und Neustartstrategie evaluieren. | Vorschlag; D-08. |

Es werden jetzt keine Dependencies ergänzt und keine neuen ADRs mit unbestätigten
Entscheidungen angelegt. Erst bestätigte Entscheidungen sind als ADR zu dokumentieren.

## Sicherheit, Risiko und Betrieb

**Vorschläge zur Konkretisierung von FR-04/FR-05:** Vor jeder Paper-Order
Positionsgröße, verfügbare Mittel, Einzelpositions- und Gesamt-Exposure,
Tagesverlust/Drawdown und maximal offene Orders prüfen. Konkrete Geld- und
Prozentlimits sind offen (D-09). Keine Hebel-/Short-Freigabe durch Default.
Kill-Switch und Pausenstatus müssen neue Orders sperren; Behandlung vorhandener
Orders/Positionen sowie Wiederfreigabe müssen separat vereinbart werden.
Ein Stop-Order-Modell garantiert bei Kurslücken keinen Ausführungspreis.

Paper- und spätere Live-Konfigurationen/Credentials strikt trennen; bei
mehrdeutiger Konfiguration Ausführung verweigern. Eine spätere Live-Freigabe
benötigt einen eigenen Auftrag, überprüfte Rechte und dokumentierte
Betriebsverantwortung; sie folgt nicht automatisch aus erfolgreichen Paper-Tests.

Für den späteren Betrieb werden strukturierte Logs mit Run-/Order-ID,
Datenfrische, Laufstatus, Risikoverletzungen, API-Fehlern und Bestandsabweichungen
vorgeschlagen. Kalenderbasierte Planung berücksichtigt Börsenfeiertage und DST;
Retries sind begrenzt und bei unbekanntem Orderstatus zunächst abzugleichen.
Paper-Journal und Datenstände benötigen Backup und getesteten Restore.
Dauerbetrieb gehört auf eine noch auszuwählende Laufzeitumgebung; Codex Cloud ist
als Entwicklungsumgebung bestätigt, nicht als unbeaufsichtigter Trading-Host.

## Risiken und Annahmen

Wahrscheinlichkeiten sind mangels Messdaten **offen**; jede Zeile benennt einen
Auslöser statt eine scheinpräzise Bewertung. Maßnahmen sind Vorschläge.

| ID | Typ / Status | Aussage / Auslöser | Auswirkung | Prüfung / Gegenmaßnahme |
| --- | --- | --- | --- | --- |
| R-01 | Risiko | Look-ahead, Survivorship Bias oder überangepasste Regeln; Auslöser: ungewöhnlich stabile Backtest-Rendite. | Unbrauchbare Strategieeinschätzung. | Point-in-Time-Daten, zeitlich getrennte Evaluation, Out-of-Sample-Prüfung und Kostenstress. |
| R-02 | Risiko | Schlechte Daten oder falsch behandelte Corporate Actions; Auslöser: Lücke, Split oder Sprung im Kurs. | Falsche Signale, Positionen und Performance. | FR-07/FR-10, Referenzfälle und Quarantäne fehlerhafter Datensätze. |
| R-03 | Risiko | Paper-Fills bilden Liquidität, Teilfüllungen, Kosten und Kurslücken unzureichend ab. | Überschätzte Umsetzbarkeit; Verluste bei späterem Live-Betrieb. | Konservative Slippage-Szenarien; Differenzen dokumentieren; keine automatische Live-Freigabe. |
| R-04 | Risiko | API-Ausfall, unbekannter Orderstatus oder Retry nach Timeout. | Doppelte Orders und inkonsistente Bestände. | Idempotenz, persistentes Journal, Abgleich vor Retry, sichere Pause. |
| R-05 | Risiko | Falsche Endpunkte oder Credentials. | Unbeabsichtigte Echtgeld-Orders. | Live-Ausführung fehlt im MVP; getrennte Paper-Ziele, Negativtests und gesperrter Fehlerfall. |
| R-06 | Risiko | Markt-, Korrelations-, Währungs- oder Gap-Risiko. | Auch diversifizierte Strategien können erhebliche Verluste erleiden. | Exposure-Limits, Kosten-/Gap-Stress und Währungsmodell; kein Renditeversprechen. |
| R-07 | Risiko | Lizenz oder Brokervertrag deckt automatisierte Nutzung, Speicherung oder Weitergabe nicht ab. | Rechtliche Folgen und Betriebsstopp. | Vor Anbieterwahl Lizenzprüfung pro Markt/Nutzung; ohne Rechte keine Beschaffung/Weitergabe. |
| R-08 | Risiko | Nutzung für Dritte, Vermögensverwaltung oder öffentliche Signale ändern regulatorische Pflichten. | Mögliche Erlaubnis-, Dokumentations-, Datenschutz- und Haftungspflichten. | Nutzerkreis/Jurisdiktion klären; qualifizierte rechtliche Prüfung vor solchem Betrieb; private Nutzung nicht als Ausnahme unterstellen. |
| R-09 | Risiko | Steuern, Gebühren, FX und Datenabonnements übersteigen angenommene Kosten. | Falsche Wirtschaftlichkeitsbewertung. | Budget und steuerlichen Kontext klären; Brutto-/Nettoannahmen trennen. Keine Steuerberatung durch das Produkt voraussetzen. |
| R-10 | Risiko | Weltweite Abdeckung im ersten Release; Auslöser: weitere Märkte vor stabiler Referenzkette. | Scope, Datenkosten und Kalenderkomplexität wachsen. | Begrenzten MVP bestätigen, Erweiterungen später einzeln bewerten. |
| A-01 | Annahme | Private, technisch versierte Eigennutzer sind erste Zielgruppe. | UX und rechtliche Grenzen könnten falsch zugeschnitten sein. | Nutzerinterview zu heutigem Ablauf, Jurisdiktion und Nutzung für Dritte; D-01. |
| A-02 | Annahme | Tagesdaten reichen für erste Swing-Strategie und Paper-Evaluation. | Intraday-Risikoregeln oder Fills könnten zusätzliche Daten benötigen. | Referenzstrategie und Orderzeitpunkte spezifizieren; D-02/D-06. |
| A-03 | Annahme | Ein erschwingliches, ausreichend lizenziertes Daten-/Paper-Angebot ist verfügbar. | MVP kann an Budget, Zulassung oder Datenrechten scheitern. | Tarif-/Rechteprüfung und später isolierter Adapter-Prototyp nach gesondertem Auftrag; D-03. |

## Offene Entscheidungen

Verantwortliche sind vorgeschlagene Rollen; eine konkrete personelle Zuordnung
ist noch offen. Keine Zeile legt eine Architektur verbindlich fest.

| ID | Frage | Optionen / Empfehlung | Benötigte Evidenz | Verantwortlich |
| --- | --- | --- | --- | --- |
| D-01 | Wer nutzt das Produkt, in welcher Jurisdiktion und ausschließlich für eigene Rechnung? | Private Eigennutzung als Annahme; Nutzung für Dritte separat bewerten. | Nutzerbestätigung, Wohn-/Betriebssitz, rechtliche Einordnung. | Product Owner; konkrete Zuordnung offen. |
| D-02 | Erster Markt, Universum, Währung, Handelsfrequenz und Scope? | Vorschlag: liquide US-Aktien, USD, Long-only, ungehebelt, Tagesdaten. | Strategiebedarf, verfügbare Daten, Nutzerbestätigung. | Product Owner; offen. |
| D-03 | Welche Daten-/Brokeranbieter und welches Budget? | Alpaca/IBKR und separaten Datenanbieter evaluieren; keine Auswahl beschlossen. | Aktuelle offizielle Dokumentation, Lizenz, Kontozulassung, Historie, Limits und Gesamtkosten. | Product Owner mit Architekturberatung; offen. |
| D-04 | Welche Datenverarbeitung und Datenformate? | pandas vs. Polars, Parquet als Kandidat. | Referenzdatensatz, Corporate-Action-Modell und Benchmark. | Architekturrolle; offen. |
| D-05 | Wie werden Kernmodell und Adapterverträge geschnitten? | Modularer Monolith mit typisierten Ports als Vorschlag. | Zwei Anbieterprofile, Statusmodell, Geld-/Rundungsregeln und Contract-Test-Entwurf. | Architekturrolle; offen. |
| D-06 | Welche Referenzstrategie und Backtest-Engine? | Transparente regelbasierte Strategie; Engine erst nach fachlichem Vergleich. | Eindeutige Signal-/Fill-Zeitpunkte, Kostenmodell, Dividendensemantik und Lizenz. | Product Owner und Architekturrolle; offen. |
| D-07 | Persistenz und Reproduzierbarkeit? | SQLite vs. PostgreSQL, versionierte Rohdaten und Run-Metadaten. | Schreibparallelität, Größenordnung, Backup-/Restore-Test. | Architektur-/Betriebsrolle; offen. |
| D-08 | Wo und wie läuft Paper-Trading dauerhaft? | Einzelner Worker mit CLI; Scheduler/Hosting noch auswählen. | Betriebsbudget, Datenrechte, API-Sitzung, Alarmkanal und Verantwortlichkeit. | Betriebsrolle; offen. |
| D-09 | Konkrete Kapital-, Positions-, Verlust- und Pausenregeln? | Zunächst konservative konfigurierbare Paper-Limits, keine Werte beschlossen. | Paper-Startkapital, gewünschte Exposure-Grenzen, Verhalten offener Orders und Wiederfreigabe. | Product Owner; offen. |
| D-10 | Zeitplan und Abnahmewerte? | PG-01 und NFR-Zielwerte als Diskussionsbasis. | Budget, Zeit, Referenzhardware, Benchmark und zulässige Fehlertoleranzen. | Product Owner mit Betriebsrolle; offen. |

## Bestätigungen und nächste Klärung

**Bestätigt durch Q-01/Q-02:** Python, internationale Aktien als Langfristziel,
Swing-Trading, mehrere regelbasierte Strategien, historische Daten/Backtesting,
Portfolio-/Risikomanagement, Brokerunabhängigkeit, zunächst Paper-Trading,
keine Echtgeld-Orders in Entwicklung/Tests und Live-Automation nur nach expliziter
Freigabe. Codex Cloud, GitHub, GitHub Projects und Factory-Standards sind gesetzt.

**Noch zu bestätigen:** Zielgruppe, Jurisdiktion, konkreter MVP-Zuschnitt,
Referenzstrategie, Anbieter, Budget, Architektur-/Technologieoptionen und sämtliche
neu vorgeschlagenen Zielwerte. Die Rückfragen zum ersten Markt und Nutzerkreis
wurden gestellt; ohne Antwort bleiben D-01/D-02 offen. Für Discovery kann mit diesen
offenen Punkten gearbeitet werden; vor einer späteren Umsetzung müssen die dafür
relevanten Entscheidungen geklärt werden. Kein Backlog wurde erstellt.

## Validierung dieses Auftrags

Die nachfolgenden Prüfungen betreffen Initialisierung, bestehende Werkzeuge und
Paketierbarkeit. Sie belegen keine Trading-Funktionalität, Datenqualität eines
Anbieters oder Brokerkompatibilität.

Ausgeführt am 2026-10-31 mit uv 0.12.23 und Projektinterpreter Python 3.12.15
(System-`python3` für den Bootstrap: 3.12.14):

| Prüfung | Ergebnis |
| --- | --- |
| Vorhandenes Bootstrap-Skript mit Projekt-/Paketname `gbdj` | Erfolgreich; Wiederholung meldet unveränderte Initialisierung. |
| `uv sync --locked` und Import von `gbdj` | Erfolgreich; Distribution `gbdj==0.1.0`. |
| `uv run --locked ruff format --check .` | Bestanden; 30 Dateien bereits formatiert. |
| `uv run --locked ruff check .` | Bestanden. |
| `uv run --locked mypy src` und `uv run --locked mypy scripts` | Beide bestanden, jeweils eine Quelldatei. |
| `uv run --locked pytest` | 48 Tests bestanden, keine fehlgeschlagen oder übersprungen; Coverage 96,15 %, Untergrenze 85 %. |
| `uv build` | sdist und Wheel für `gbdj` erfolgreich erstellt. |

Der erste Lauf nach Initialisierung hatte vier fehlgeschlagene und 43 bestandene
Tests sowie 61,54 % Coverage: Die bestehende `pristine`-Fixture ersetzte Projekt-
und Paketnamen global nacheinander. Bei identischen Namen blieb dadurch eine
ungültige Template-Konfiguration zurück. Die Fixture rekonstruiert jetzt nur
die konkreten Metadatenmarker und eine minimale Template-README. Der bisher im
initialisierten Projekt verkürzte Initialisierungstest durchläuft wieder den
vollständigen Bootstrap inklusive Offline-Installation und Import. Ein zusätzlicher
Test prüft die unveränderte Produkt-README beim erneuten Bootstrap mit `gbdj`.
Das Bootstrap-Skript selbst wurde nicht geändert; keine Assertions oder
Coverage-Grenzen wurden abgeschwächt. Der abschließende Lauf besteht vollständig.

Nicht ausgeführt: Trading-/Broker-/Live-Tests mangels Implementierung; kein
Backtest und keine Paper-Sitzung. Offizielle Anbieterquellen konnten wegen
Netzwerksperren nicht geprüft werden. Lokaler GitHub-Actions-Lauf wurde nicht
behauptet; die obigen Repository-Befehle wurden in Codex Cloud ausgeführt.
