# Veröffentlichungsplan: GlobalStockBot GitHub Issues und Projects

Status: **Zur Freigabe; nichts veröffentlicht; keine Implementierung freigegeben.**
Basis: aktueller `origin/main`, Commit `41e71c774869aaeb0da0f085df522cc25ad44880`
(Merge von Planungs-PR #2). Git-Read funktioniert. Dieser Plan liegt auf dem
separaten Branch `docs/gbdj-publication-plan`, unmittelbar von diesem main-Stand.

## Quellen und Freigabegrenzen

Grundlage sind [Product Brief](product-brief.md), [Backlog](backlog.md),
[MVP-Roadmap](mvp-roadmap.md), alle 32 [Issue-Entwürfe](issues/) und der bestehende
Skill `backlog-refinement` samt Referenz/Vorlage sowie zentrale Issue-Vorlagen.
Die alten Angaben zur gestapelten PR-Basis im Backlog beschreiben die damalige
Planung; sie werden nicht als aktuelle Git-Basis übernommen.

Der aktuelle Auftrag autorisiert **Prüfung und Veröffentlichungsvorbereitung**.
Eine Freigabe zur Veröffentlichung muss die konkreten IDs und den vorgesehenen
Inhalt bezeichnen. Sie erlaubt das Anlegen/Verknüpfen im Backlog, nicht die
Umsetzung, Architekturwahl, Datenbeschaffung, Brokeranbindung oder Live-Ausführung.
Alle fachlichen Vorschläge und offenen Entscheidungen behalten ihren Status.
Auch ein Project-Status Backlog ist weder DoR noch ein Implementierungsauftrag.

## Prüfung der vorhandenen Entwürfe

- Sieben Epics, 15 Stories und zehn Tasks: 32 eindeutige IDs und Titel;
  null identische Titel/Dateibodys und inhaltlich keine erkennbaren lokalen Dubletten.
- Alle vorhandenen Vorlagenüberschriften, Nutzen/Scope/Nicht-Ziele,
  nummerierten Kriterien, Quellen, Prioritäten, Größen und Risiken sind enthalten.
  Jeder Einzelauftrag gehört zu genau einem der sieben Epics; die Zuordnung ist
  mit den Epic-Kinderlisten konsistent.
- 25 Einzelaufträge mit gültigen Vorgänger-IDs, ohne Zyklen; die Backlog-Reihenfolge
  ist topologisch gültig. Epic-Hierarchie und fachliche Blockierung sind getrennt.
- Die bestätigten Produktanforderungen sind über die Matrix im Backlog zugeordnet.
  FR-01 (internationale Märkte) und mehrere produktive Strategien bleiben langfristig;
  der MVP verwirklicht bewusst nur einen begrenzten ersten Schnitt.
- S-02, S-05, S-10 und S-11 sind keine Dubletten: Referenz-Handelsrunde,
  Kosten-/Mehrinstrumentbacktest, persistente Paper-Sitzung und Fehlerwiederanlauf
  liefern unterschiedliche Outcomes. Der minimale Referenzpfad wird erweitert,
  nicht parallel ein zweites Handelssystem gebaut.
- Keine neuen Bugs erfunden. S-14/S-15 sind L-Platzhalter: für einen Backlog
  veröffentlichbar, aber vor Implementierung weiter zu schneiden. Alle Einträge
  sind mangels konkreter Umsetzungsfreigabe weiterhin **nicht Ready**.

**Zu beachten, ohne die Entwürfe still zu ändern:** T-01 soll offene Entscheidungen
klären, verlangt aber pauschal, diese vor Umsetzung geklärt zu haben. Für die spätere
Beauftragung eines Klärungstasks müssen seine offenen Fragen als Input zulässig
sein; sein Abschluss erfindet keine Zustimmung. Dasselbe Prinzip gilt für
T-02/T-03/T-05/T-06. Das blockiert die Veröffentlichung als Vorschlag nicht.
Die konkreten Risiko- und Betriebszielwerte müssen vor Implementierung bestätigt
werden. Mengen-/Umfangsschätzungen der L-Einträge sind keine Terminversprechen.

**Online-Dublettenstatus: ungeprüft.** Die GitHub-Lesebefehle scheitern derzeit.
Die Prüfung aller offenen und geschlossenen Repository-Issues ist vor jeder
Veröffentlichung zwingend nachzuholen. Es wird nicht unterstellt, dass im
Repository noch keine Issues existieren.

## Vollständige Übersicht der vorgesehenen Issues

Titel auf GitHub: `[ID] [Epic|Story|Task] Titel`. Die Titel-/ID-Konvention erlaubt
verlässliche Zuordnung ohne erfundene GitHub-Nummern. MVP-Angaben und Prioritäten
sind aus den Entwürfen übernommen. Epic-Abschluss umfasst alle Kinder, nicht nur M1.

| ID | Titel | Typ | Parent | Priorität | MVP-Zuordnung | Fachliche Abhängigkeiten |
| --- | --- | --- | --- | --- | --- | --- |
| [E-01](issues/E-01.md) | Verlässliche historische Aktienbasis | Epic | — | P1 | MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-02](issues/E-02.md) | Nachvollziehbare Strategieexperimente | Epic | — | P1 | MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-03](issues/E-03.md) | Kontrolliertes Portfolio und Risiko | Epic | — | P1 | MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-04](issues/E-04.md) | Lokales Paper-Trading ohne Echtgeldwirkung | Epic | — | P1 | MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-05](issues/E-05.md) | Überprüfbare Ergebnisse und begleiteter Betrieb | Epic | — | P1 | MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-06](issues/E-06.md) | Weitere Strategien und internationale Märkte | Epic | — | P2 | Nach MVP | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [E-07](issues/E-07.md) | Entscheidungsgrundlage für spätere Broker und Live-Freigabe | Epic | — | P2 | Nach MVP / Untersuchung | keine pauschalen Epic-Gates; Kindabhängigkeiten separat |
| [T-01](issues/T-01.md) | MVP klären und Abnahmevertrag festhalten | Task | E-01 | P1 | MVP / Gate G0 | keine |
| [T-02](issues/T-02.md) | Datenrechte und historisches Eingabeformat prüfen | Task | E-01 | P1 | MVP / Gate G0 | T-01 |
| [T-03](issues/T-03.md) | Minimale Kernverträge und Replay-Schnittstellen entscheiden | Task | E-02 | P1 | MVP / Gate G0 | T-01 |
| [T-04](issues/T-04.md) | Offline-Ausführungsmodus gegen Live-Aufrufe absichern | Task | E-04 | P1 | MVP / M1 | T-03 |
| [S-01](issues/S-01.md) | Historische Tagesdaten aus einer lokalen Datei einlesen | Story | E-01 | P1 | MVP / M1 | T-02, T-03 |
| [S-02](issues/S-02.md) | Ersten historischen Kauf-Verkauf-Ablauf durchspielen | Story | E-02 | P1 | MVP / M1 | T-04, S-01 |
| [S-03](issues/S-03.md) | Unvollständige und widersprüchliche Tagesdaten zurückweisen | Story | E-01 | P1 | MVP / M2 | S-01 |
| [S-04](issues/S-04.md) | Eine einfache Swing-Strategie konfigurieren und Signale berechnen | Story | E-02 | P1 | MVP / M2 | S-02 |
| [S-05](issues/S-05.md) | Historische Mehrinstrument-Läufe mit Kosten auswerten | Story | E-02 | P1 | MVP / M2 | S-03, S-04 |
| [S-06](issues/S-06.md) | Positionen und Cash nach simulierten Fills bewerten | Story | E-03 | P1 | MVP / M2 | S-05 |
| [S-07](issues/S-07.md) | Orderabsichten vor Ausführung gegen Kapital- und Positionslimits prüfen | Story | E-03 | P1 | MVP / M3 | S-06, T-01 |
| [S-08](issues/S-08.md) | Verlustgrenzen und Pausenstatus durchsetzen | Story | E-03 | P1 | MVP / M3 | S-07 |
| [S-09](issues/S-09.md) | Splits und Dividenden in einer Referenzhistorie korrekt behandeln | Story | E-01 | P1 | MVP / M3 | S-03, S-06 |
| [T-05](issues/T-05.md) | Persistenzvertrag für das lokale Paper-Journal entscheiden | Task | E-04 | P1 | MVP / vor M3 | T-03 |
| [S-10](issues/S-10.md) | Lokale Paper-Sitzung schrittweise und persistent ausführen | Story | E-04 | P1 | MVP / M3 | S-07, S-04, T-05 |
| [S-11](issues/S-11.md) | Paper-Lauf nach Unterbrechung konsistent abgleichen | Story | E-04 | P1 | MVP / M4 | S-10 |
| [S-12](issues/S-12.md) | Backtest und Paper-Ergebnisse nachvollziehbar berichten | Story | E-05 | P1 | MVP / M4 | S-06, S-09, S-11 |
| [T-06](issues/T-06.md) | Betriebs- und Evaluationsvertrag festlegen | Task | E-05 | P1 | MVP / vor M4 | T-01 |
| [S-13](issues/S-13.md) | Lokale Paper-Läufe planen und Fehler sichtbar machen | Story | E-05 | P1 | MVP / M4 | T-06, S-11, S-08 |
| [T-07](issues/T-07.md) | Backup, Restore und Störungsnachweise für Paper-Betrieb erbringen | Task | E-05 | P1 | MVP / M4 | S-13, S-12, S-08 |
| [T-08](issues/T-08.md) | Historische Evaluation und Paper-Abnahme dokumentieren | Task | E-05 | P1 | MVP / M5 | T-07, S-05, S-09, S-12 |
| [S-14](issues/S-14.md) | Zweite regelbasierte Strategie getrennt vergleichen | Story | E-06 | P2 | Nach MVP | T-08 |
| [S-15](issues/S-15.md) | Zusätzlichen Aktienmarkt mit Kalender und Währung auswerten | Story | E-06 | P2 | Nach MVP | T-08 |
| [T-09](issues/T-09.md) | Offizielle Broker-Paper-APIs und Zulässigkeit vergleichen | Task | E-07 | P2 | Nach MVP / Untersuchung | T-08 |
| [T-10](issues/T-10.md) | Freigabekriterien für möglichen Live-Handel untersuchen | Task | E-07 | P3 | Nach MVP / nur Freigabekatalog | T-09 |

## Veröffentlichungspakete zur Auswahl

Keine Auswahl ist bereits genehmigt. Der Nutzer kann auch eine genaue Teilmenge
bestätigen; Parents/Vorgänger müssen dann vorhanden sein oder gesondert geklärt
werden. Die folgenden Pakete sind vollständig bezüglich ihrer Parent-/Vorgänger-IDs.

| Paket | Umfang | Zweck / Empfehlung |
| --- | --- | --- |
| **A – M1 inklusive G0 (empfohlen)** | **9 Issues:** E-01, E-02, E-04; T-01, T-02, T-03, T-04, S-01, S-02 | Kleinster Veröffentlichungsstart für den ersten End-to-End-Meilenstein. |
| B – gesamter MVP | **26 Issues:** E-01 bis E-05; T-01 bis T-08; S-01 bis S-13 | Gesamte Daten-/Backtest-/Risiko-/Paper-/Betriebsevaluation sichtbar machen. |
| C – gesamtes Product Backlog | **32 Issues:** E-01 bis E-07; T-01 bis T-10; S-01 bis S-15 | Zusätzlich die späteren L-Stories und Broker-/Live-Untersuchungen als unfreigegebene Zukunftseinträge. |

**Erster Meilenstein M1:** Nach Roadmap sind die direkten M1-Aufgaben T-04, S-01
und S-02. Ihre vollständige Vorgängerkette enthält T-01, T-02 und T-03 (Gate G0).
Dazu gehören E-01, E-02 und E-04 als Parent-Issues. Reihenfolge nach Elternanlage:
T-01 → T-02/T-03 → T-04/S-01 → S-02; T-04 benötigt T-03, S-01 beide T-02/T-03.

Ergebnis von M1: lokale Kursdatei, feste Referenzsignale, genau eine simulierte
Kauf-/Verkauf-Runde mit minimalem Kapitalcheck und handgerechneter Ausgabe.
M1 enthält noch **keine konfigurierbare Strategie, vollständigen Risikoregeln oder
persistenten Paper-Betrieb** und ist daher nicht die gesamte MVP-Abnahme.
Ein GitHub-Milestone-Objekt wird ohne gesonderte Zustimmung nicht angelegt;
M1/G0 können vorerst im Issue-Body stehen.

## Autorisierte Schnittstelle und beobachtete Zugriffsgrenzen

Vorhanden ist GitHub CLI (`gh`) mit bereits gesetztem `GH_TOKEN`; Werte werden
weder ausgelesen noch protokolliert. Die Plattform-Git-Authentifizierung genügt
für Fetch/Push, beweist aber keine API-/Project-Schreibrechte.

| Lesende Prüfung | Beobachtung | Aussage |
| --- | --- | --- |
| `git fetch origin main` | Erfolgreich; SHA oben | Aktuelle main-Basis geprüft. |
| Cloud-Status und lokale Netzwerkpolicy | HTTP-Regeln aktiv, `api.github.com` nicht freigegeben | API wird vor GitHub-Authentifizierung blockiert. |
| `gh api repos/enis-j-13/gbdj --jq '{full_name,has_issues,permissions}'` | `Forbidden` | Repository-Settings/Issues-Aktivierung und API-Rechte nicht bestimmbar. |
| `gh issue list --repo enis-j-13/gbdj --state all --limit 100 --json number,title,state,url` | GraphQL-Verbindung `Forbidden` | Keine Online-Inventur und kein Dublettennachweis möglich. |
| `gh project list --owner enis-j-13 --format json --limit 100` | `unknown owner type` | CLI konnte den Owner nicht auflösen; dies beweist weder fehlendes Project noch fehlende Rechte. |

Es ist keine ausreichende direkte GitHub-Connector-Schnittstelle verfügbar.
`gh` wäre die vorgesehene API-Schnittstelle, ist aktuell jedoch nicht verwendbar.
Eine fehlende **API-Schreibberechtigung ist damit nicht bewiesen**; sie bleibt
hinter der bestätigten Netzwerksperre ungeprüft. Kein Test-Issue und kein
Test-Project-Item wird zur Rechteprüfung angelegt. Ein früher gespeicherter
Netzwerkentwurf ist nicht mit einer aktiven Freigabe gleichzusetzen.

Nach unterstützter Aktivierung des API-Zugriffs: Repository-Rechte und
Issues-Aktivierung, vollständige Issue-Inventur inklusive geschlossener Einträge,
Parent-/Sub-Issue-Fähigkeit, vorhandene Issue-Typen/Labels sowie genaues Project
mit Rolle, Feldern, Optionen und Workflows lesend prüfen. Bestehende Bindungen
verwenden; keine Tokens im Chat anfordern. Erst ein erfolgreicher genehmigter
Schreibvorgang beweist die konkrete Schreibfähigkeit.

## Zuordnung zum bestehenden GlobalStockBot Project

Project-URL, Owner und Nummer sind bisher nicht im Repository verzeichnet und
über die gesperrte API nicht feststellbar. Der Nutzer wurde nach der URL gefragt;
bis zur Antwort bleibt die Zuordnung offen. Der Name allein ist kein eindeutiger
Identifikator. Es wird weder ein Project erraten noch ein neues erstellt.

Vorgesehene Abbildung, nach Prüfung vorhandener Felder:

| Planungsinformation | Ziel / Fallback |
| --- | --- |
| Bearbeitungsstatus | Project-Feld `Status` exakt **Backlog**; Issue selbst offen. Nie automatisch Ready/In Progress. |
| Epic-Hierarchie | Epics als normale offene Parent-Issues; Stories/Tasks als native Sub-Issues. Checklisten allein erfüllen die Parent-Zuordnung nicht. |
| Typ Epic/Story/Task | Vorhandener passender Issue-Typ oder vorhandenes Label; Titel und Body behalten den Typ in jedem Fall. |
| Priorität P1/P2/P3 | Vorhandenes Prioritätsfeld passend mappen; andernfalls vorhandenes Label bzw. expliziter Wert im Body. P1/P2 nicht blind numerischen Defaultoptionen gleichsetzen. |
| MVP und Phase | Vorhandene Felder nutzen, sonst Body `MVP / G0 / M1 …` bzw. `Nach MVP`; Epic-Zuordnung ersetzt keine Phasenzuordnung. |
| Lokale ID und Quellen | Titel, stabiler Body-Marker und unveränderlicher Quelldateilink; vorhandenes ID-Feld zusätzlich nutzen. |
| Fachliche Abhängigkeiten | Immer lesbare `Benötigt: #…`-Links; native Blockierungsrelationen nur bei verfügbarer Unterstützung/Rechten. Parent ist keine Abhängigkeit. |
| Implementierungsfreigabe | Explizit **nicht erteilt** im Body; Veröffentlichung und Backlog-Zugehörigkeit ändern diesen Wert nicht. |

Neue Labels, native Typen, Project-Felder, Optionen oder Workflows werden nicht
ungefragt angelegt/geändert. Fehlt die Option Backlog oder überschreibt eine
Automation den Status, ist die Project-Zuordnung zu klären statt still auf Todo
oder Ready auszuweichen. Ebenso bleibt eine nicht herstellbare native Parent-
Relation als offener Zuordnungsschritt dokumentiert.

## Sicherer Ablauf nach konkreter Veröffentlichungsfreigabe

1. Freigegebene IDs, Inhalte, Paket, Project und Umfang der Relation-/Feldzuordnung
   mit der genauen Nutzerfreigabe im Register festhalten. Quellenhashes gegen den
   genehmigten main-Stand prüfen; bei fachlichen Änderungen neue Freigabe einholen.
2. Alle offenen/geschlossenen Issues mit vollständiger Pagination inventarisieren.
   Nach ID im Titel/Body und nach fachlich gleichem Inhalt suchen. Auch das Project
   auf bereits zugeordnete Items prüfen. Bei mehreren/abweichenden Treffern den
   betroffenen Eintrag klären; keine automatische Neuerstellung oder Fremdänderung.
3. Eindeutige vorhandene Treffer nach inhaltlichem Abgleich wiederverwenden und
   Nummer/URL registrieren; geschlossen ist kein Anlass für ein Duplikat oder
   ungefragtes Wiederöffnen. Unterschiedliche bestehende Inhalte nicht überschreiben.
4. Nur fehlende **genehmigte** Epic-Parents anlegen und die zurückgegebenen Nummern
   sofort ins Register schreiben. Danach genehmigte Kinder in topologischer
   Reihenfolge anlegen/wiederverwenden. Eltern/Kinder außerhalb des Pakets werden
   nicht automatisch mitveröffentlicht.
5. Native Parent-Relationen setzen und verifizieren; genehmigte Abhängigkeiten
   anhand der registrierten Nummern im Body und optional nativ verlinken.
   Epic-Kinderlisten als Nachweis des Pakets aktualisieren. Noch nicht veröffentlichte
   Kinder/weitere Phasen bleiben mit lokalen IDs und stabilen Quelldateilinks sichtbar,
   ohne erfundene Issue-Nummern. M1 schließt seine umfangreicheren Epics nicht ab.
6. Issues dem **bestätigten bestehenden Project** zuordnen und Status Backlog
   ausdrücklich setzen/lesen; Feldwerte und automatische Statusänderungen prüfen.
   Nicht verfügbare Projektzuordnung bleibt ausstehend. Nur wenn dieses Vorgehen
   ausdrücklich genehmigt ist, darf die reine Issue-Veröffentlichung ohne Project
   stattfinden; sonst vor der ersten Erstellung warten.
7. Nach jedem Schritt Issue-Nummer/URL, Parent, Abhängigkeiten, Project-Item-ID und
   Rücklese-Ergebnis sichern. Bei Timeout vor Retry anhand stabiler ID/Marker
   abgleichen: ein möglicherweise erstelltes Issue nicht blind erneut anlegen.
   Keine automatischen Löschungen als Rollback, keine doppelten Issues.
8. Abschlussbericht getrennt für angelegt/wiederverwendet, Relationsstatus,
   Project/Backlog-Status und verbleibende Fehler. Null Implementierungsfreigaben,
   keine Zuweisung zu einem Entwickler oder Sprint ohne Auftrag.

Die vorgesehene anfängliche State-/Metadatenpflege und Verknüpfung bereits
passender Issues muss vom Veröffentlichungspaket umfasst sein; es ist keine
Freigabe zur beliebigen Änderung bestehender Issues.

## Nachvollziehbare manuelle Alternative

Die manuelle Variante verwendet dieselben genehmigten IDs und dieselbe
Dublettenprüfung, keine reduzierte zweite Backlog-Quelle.

- [Manifest](issue-publication-manifest.json): enthält für alle 32 Einträge Titel,
  Metadaten, Parent, Vorgänger, Quellenhash und vorbereiteten Markdown-Body.
  Quelldateilinks wurden in absolute GitHub-Links auf den geprüften main-Commit
  umgewandelt, damit sie auch außerhalb des Dateiverzeichnisses funktionieren.
- [Register](issue-publication-register.csv): vollständige Inventarliste mit noch
  leeren GitHub-Nummern/URLs und Project-Item-IDs sowie ausstehenden Freigaben.
  Eine leere Nummer bedeutet nicht „Issue fehlt online“, sondern „noch nicht abgeglichen“.
- Nach Freigabe in GitHub zunächst nach ID und Inhalt suchen. Dann `New issue`
  im Repository öffnen, genehmigten Manifest-Titel/Body übernehmen und den
  Veröffentlichungsvermerk mit der tatsächlichen Freigabe aktualisieren.
  Implementierungsfreigabe bleibt unverändert „nicht erteilt“.
- Epic-Parents zuerst erstellen oder wiederverwenden; danach jedes Kind über
  GitHubs Sub-Issue-Funktion zuordnen. Mit tatsächlichen `#Nummern` die Vorgänger
  und die bereits veröffentlichten Epic-Kinder ergänzen. Quellen-/Anforderungslinks
  und nicht veröffentlichte lokale IDs bleiben erhalten.
- Im bestätigten bestehenden GlobalStockBot Project hinzufügen und Status Backlog
  wählen. Fehlende Rechte/Felder nicht durch ein neues Project ersetzen. Nur das
  genehmigte Verhalten bei fehlender Project-Zuordnung anwenden.
- Nach jeder Erstellung/Zuordnung das CSV-Register mit der tatsächlichen Nummer,
  URL, Project-Item-ID (soweit lesbar) und Ergebnis ergänzen. Ohne lesbare Item-ID
  mindestens Project-/Issue-URL plus manuelle Statusprüfung als Nachweis erfassen;
  die ID bleibt ausdrücklich unbekannt. Nach einem abgebrochenen Schritt zuerst
  abgleichen und dann fortsetzen. Keine ID doppelt veröffentlichen.

Das Manifest ist **kein ausführendes Importskript**. Seine Freigabewerte stehen
auf false und alle Online-IDs auf null. Der vorbereitete Body hat vorläufige
Freigabevermerke; vor genehmigtem Versand werden nur diese Vermerke und bekannte
Relationen aktualisiert, keine ACs oder fachlichen Entscheidungen still geändert.

## Offene Entscheidungen für die Freigabe

1. **Paket:** A (neun, empfohlen), B (26), C (32) oder exakt benannte Teilmenge.
2. **Zielproject:** tatsächliche URL/Owner/Nummer des bestehenden GlobalStockBot
   Projects; ein passender Name allein reicht nicht.
3. **Bei fehlenden Project-Rechten:** auf vollständige Zuordnung warten oder
   ausdrücklich nur genehmigte Repository-Issues anlegen und Project-Schritte
   als ausstehend dokumentieren. Empfehlung: bis zur Klärung warten.
4. **Metadaten:** vorhandene passende Felder/Labels wiederverwenden; wenn sie
   fehlen, Typ/Priorität/Phase im Body erhalten. Neue Felder/Labels/Workflows nur
   nach gesonderter konkreter Zustimmung. Native Epic-/Sub-Issue-Beziehung bleibt Ziel.
5. **Technische Voraussetzung:** aktiver API-Zugriff und passende Repository-
   Issues-/Projects-Rechte. Eine fachliche Freigabe allein hebt Netzwerksperren
   oder fehlende Berechtigungen nicht auf.

Markt, Jurisdiktion, Datenquelle, Strategie, Engine, Persistenz, Risikolimits und
konkrete Betriebs-/Abnahmeziele bleiben wie bisher vor den jeweiligen
Implementierungsaufträgen zu klären. Sie müssen nicht durch eine reine
Backlog-Veröffentlichung als entschieden erklärt werden.

Eine mögliche konkrete Freigabe lautet:

> Veröffentlichungspaket A mit genau E-01, E-02, E-04, T-01, T-02, T-03,
> T-04, S-01 und S-02 als offene Backlog-Issues ist freigegeben, einschließlich
> Wiederverwendung inhaltlich passender bestehender Issues, Parent-/Sub-Issue-
> Zuordnung und Verlinkung der genehmigten Abhängigkeiten. Zielproject: [URL].
> Bei fehlender Project-Zuordnung zunächst warten. Keine Implementierung freigegeben.

Dies ist ausschließlich ein Formulierungsvorschlag, keine bereits erteilte Freigabe.

## Prüfstatus der Vorbereitung

Struktur, Kriteriennummerierung, Quellenlinks, Parent-Konsistenz, eindeutige
IDs/Titel, zyklusfreie/topologische Abhängigkeiten sowie abgeschlossene
Paket-Auswahlen geprüft. Inhaltliche Trennung der überlappenden Referenz-/Paper-
Fälle geprüft. Online-Dubletten und Projects bleiben wegen API-Sperre ungeprüft.
Keine Issues, Parent-Relationen oder Project-Items wurden testweise geschrieben.
Neue Python-Anwendung, Brokerverbindungen, Orders und Skills wurden nicht erstellt.
Aktuell ausgeführte Repository-Prüfungen für diesen Dokumentations-/Exportdiff:
Ruff-Formatcheck (65 Dateien), Ruff-Lint und beide mypy-Prüfungen für src/scripts
bestanden; pytest: **48 bestanden, keine fehlgeschlagenen oder übersprungenen
Tests, 96,15 % Coverage** bei 85 % Untergrenze und Python 3.12.15. Die Exportprüfung
bestätigt 32 eindeutige Einträge, unveränderte Quellenhashes/ACs, Paketgrößen
9/26/32 und vollständige Parents/Vorgänger pro Paket. Es gibt keine auf true
gesetzten Veröffentlichungs-/Implementierungsfreigaben und keine erfundenen
GitHub-Nummern. Git-Whitespace-Prüfung bestanden.

Paketbau nicht erneut ausgeführt: Anwendung, Manifest/Lockfile der Python-
Dependencies und Paketierung bleiben unverändert. Keine Tests bloß zur
Spiegelung der Dokumentation hinzugefügt. Diese Prüfung weist keine API-
Schreibberechtigung und keine Handelsfunktion nach; die alten Testergebnisse
aus dem Backlog wurden nicht als aktuelle Ausführung übernommen.
