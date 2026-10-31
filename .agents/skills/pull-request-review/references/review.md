# Review-Methode

## Prüfumfang
- Vergleiche den Feature-Diff zur vereinbarten Base, üblicherweise dem Merge-Base
  mit main. Prüfe auch Migrationen, Konfiguration und gelöschte Dateien im Diff.
- Ordne jedes Akzeptanzkriterium einem Nachweis oder einer expliziten Lücke zu.
- Prüfe neue Logik über ihre Aufrufer: Eingabeverträge, Rückgaben, Seiteneffekte,
  Fehlerpfade und Kompatibilität. Verwechsle vorhandene Defekte nicht mit neu
  eingeführten oder verschärften Problemen.
- Bewerte Typen, Modulgrenzen, Ressourcennutzung und Wartbarkeit anhand konkreter
  Auswirkungen. Umfangreiche Abstraktionen sind nicht automatisch bessere Architektur.
- Prüfe Sicherheitsgrenzen gezielt: Eingabevalidierung, Pfad- und Shell-Verarbeitung,
  Berechtigungen, Secrets/Logs, TLS und neue Dependencies. Keine Geheimnisse wiedergeben.
- Prüfe Tests auf sinnvolle Assertions, Fehlerfälle, Isolation und ausgelassene
  Risiken. Coverage allein beweist weder Korrektheit noch erfüllte Akzeptanzkriterien.
- Vergleiche Änderungen mit dem Auftrag: unnötige Refactorings, Lockfile-Abweichungen,
  generierte Artefakte und versehentlich mitgeänderte Dateien benennen.

## Schweregrade
| Grad | Bedeutung | Umgang |
| --- | --- | --- |
| P0 · kritisch | Belegter unmittelbarer schwerer Schaden, z. B. offengelegtes Secret oder destruktiver Standardpfad | Sofort behandeln; Empfehlung: nicht mergen |
| P1 · hoch | Wesentliche Kriterien verletzt, Sicherheitslücke oder wahrscheinlicher Datenverlust im relevanten Ablauf | Vor Merge beheben |
| P2 · mittel | Reproduzierbarer begrenzter Fehler, relevante Testlücke oder konkrete Wartbarkeitsgefahr | Korrektur empfehlen und Wirkung erklären |
| P3 · niedrig | Kleine standardbezogene Verbesserung ohne wesentliche Verhaltensauswirkung | Nicht blockierende Empfehlung |

Schweregrad folgt der nachgewiesenen Auswirkung, nicht persönlicher Präferenz.
Bei Unsicherheit eine offene Frage mit benötigtem Nachweis statt eines sicheren
Defekturteils formulieren. Doppelte Ursachen zu einem Befund bündeln.

## Beispielbefund
`P1 · hoch · src/example/export.py:42`: Ein vorhandener Zielpfad wird vor der
Validierung überschrieben. Bei einer ungültigen Eingabe gehen bestehende Daten
verloren (AC-2: keine Ausgabe bei Fehler). Erst validieren, dann atomar schreiben;
Regressionstest mit bestehender Datei und ungültiger Eingabe ergänzen.

Der Beispielpfad ist illustrativ. Tatsächliche Berichte benötigen reale Pfade
und Zeilen aus der geprüften Revision sowie nachvollziehbare Reproduktion.
