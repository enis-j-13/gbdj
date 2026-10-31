# Teststandards

- Verwende pytest und benenne Tests nach beobachtbarem Verhalten.
- Teste reguläre Fälle, relevante Grenzfälle und erwartete Fehler.
- Halte Unit-Tests deterministisch, isoliert und ohne externen Netzwerkzugriff.
  Verwende temporäre Verzeichnisse für Dateisystemtests und sichere vorhandene Daten.
- Prüfe Ergebnisse und Seiteneffekte; reine Aufrufzählungen genügen selten.
- Änderungen am Bootstrap brauchen Tests für gültige und ungültige Namen,
  wiederholte Ausführung und den Schutz vorhandener Dateien.
- Führe die relevanten Tests tatsächlich aus. Unterscheide bestandene,
  fehlgeschlagene, übersprungene und nicht ausgeführte Prüfungen.
- pytest-cov misst Branch-Coverage für Anwendung und Bootstrap. Die gemeinsame
  Mindestabdeckung beträgt 85 %. Ergänze sinnvolle Tests statt Ausnahmen zur
  Umgehung der Grenze; Coverage ersetzt keine fachlichen Assertions.
