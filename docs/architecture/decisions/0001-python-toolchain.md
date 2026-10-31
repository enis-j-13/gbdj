# ADR 0001: Python-Toolchain und Repository-Struktur

Status: Angenommen

## Kontext

Die Factory soll kleine und größere Python-Projekte ohne Framework-Vorgaben
starten können. Lokale Entwicklung, Codex Cloud und CI brauchen dieselben Prüfungen.

## Entscheidung

Python 3.12 ist die Startversion (`.python-version`, CI, Ruff und mypy).
`requires-python >=3.12` definiert die Mindestversion; höhere Versionen sind
noch nicht durch eine CI-Matrix garantiert. uv verwaltet eine Dev-Dependency-Gruppe
und das versionierte Lockfile. Hatchling baut das Paket nach PEP 517/518 und
PEP 621. Das src-Layout stellt sicher, dass Tests das installierte Paket importieren.

Ruff übernimmt Formatierung, Linting und NumPy-Docstrings, mypy prüft strikt,
pytest und pytest-cov prüfen Verhalten und Abdeckung. CI führt dieselben Befehle
wie die Dokumentation aus. Die uv-Version ist in CI explizit festgelegt.

Der Bootstrap verändert nur bekannte Platzhalter in vier Textdateien und
verschiebt das Paket. Er führt weder Git- noch Netzwerkoperationen aus.
Die Umbenennung im Lockfile ändert nur den lokalen Projekt-Eintrag und erhält
die gesperrten Abhängigkeiten. Tests prüfen anschließend die uv-Konsistenz offline.

## Folgen

Kein Dienst muss gestartet werden. Frameworks, Datenbanken, Docker und Codex Skills
bleiben außerhalb von Phase 1. Dependency-Upgrades erfolgen bewusst mit aktualisiertem
Lockfile. Die Bootstrap-Ausführung ist vor eigenen Strukturänderungen vorgesehen;
fehlende oder mehrdeutige Marker führen zum Abbruch vor Änderungen.
