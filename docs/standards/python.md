# Python-Standards

Diese Regeln gelten unabhängig von Framework und Anwendungsdomäne.

- Befolge PEP 8, PEP 257 und PEP 484. Die Zeilenlänge beträgt 88 Zeichen.
  Ruff formatiert und prüft den Code; NumPy ist die Docstring-Konvention.
- Verwende Type Hints für Funktionsparameter, Rückgaben und öffentliche APIs.
  Vermeide `Any`, wenn ein konkreter Typ oder ein Protokoll möglich ist.
- Dokumentiere öffentliche Module, Klassen und Funktionen. Beschreibe bei
  nichttrivialen APIs Parameter, Rückgaben, Fehler und relevante Seiteneffekte
  mit NumPy-Abschnitten (`Parameters`, `Returns`, `Raises`). Wiederhole keine
  offensichtlichen Details aus dem Code.
- Schreibe kleine, klar verantwortliche und unabhängig testbare Funktionen.
  Trenne Berechnung und Transformation von Datei-, Netzwerk- und Prozesszugriffen.
- Verwende sprechende `snake_case`-Namen. Geeignete Funktionspräfixe sind
  `get_` für Zugriff ohne externe I/O, `read_` und `write_` für I/O,
  `calculate_` für Berechnungen, `transform_` für Umwandlungen,
  `validate_` für Validierung, `build_` für Konstruktion und `run_` für Abläufe.
  Wähle die passende Bedeutung; erzwinge kein Präfix für Protokollmethoden.
  Verwende **kein `load_` als Funktionspräfix**.
- Halte Modulgrenzen fachlich nachvollziehbar und Abhängigkeiten explizit.
  Vermeide zirkuläre Imports, versteckten globalen Zustand und unnötige Abstraktionen.
- Validiere fremde Eingaben an Systemgrenzen. Fange nur erwartete Exceptions;
  gib Fehler mit Kontext weiter und erhalte die Ursache mit `raise ... from ...`.
  Verwende keine stillen Fallbacks, die fehlerhafte Ergebnisse als Erfolg darstellen.
- Nutze Kontextmanager für Ressourcen und `pathlib` für Dateipfade. Behandle
  Encoding, Zeitzonen und Rundung explizit, wenn sie das Verhalten beeinflussen.
- Protokolliere keine Secrets oder sensiblen Nutzdaten. Verwende keine
  deaktivierte TLS-Prüfung und keine unvalidierten Shell-Interpolationen.
- Halte Dependencies begründet und minimal. Framework- und Domänenregeln gehören
  in die jeweilige Projektdokumentation, nicht in diesen allgemeinen Standard.

Namenssemantik und Modulgrenzen werden im Review geprüft; Ruff ersetzt diese
inhaltliche Prüfung nicht. Tests folgen [testing.md](testing.md).
