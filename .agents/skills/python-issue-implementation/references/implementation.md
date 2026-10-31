# Checkliste für genau ein Issue

## Auftrag und Plan
- Identität, Quelle/Stand und ausdrückliche Freigabe des Issues festhalten.
- Akzeptanzkriterien nummerieren, ohne ihren Inhalt stillschweigend zu ändern.
- Bestehende Module, öffentliche Schnittstellen und Fehlerpfade identifizieren.
- Bestehende lokale Änderungen erhalten; keine pauschalen Resets oder Clean-Befehle.
- Plan auf wenige konkrete Schritte begrenzen: Änderung, Test, erwarteter Nachweis.
- Ist eine ungeklärte Produktentscheidung nötig, die Frage und ihre Auswirkung
  nennen. Unabhängige Analyse fortsetzen, aber die Entscheidung nicht erfinden.

## Umsetzung und Nachweis
- Tests nach Verhalten ausrichten; relevante Fehler- und Grenzfälle prüfen.
- Für einen Bug möglichst zuerst einen reproduzierenden Regressionstest ausführen.
- Ergebnisse den Akzeptanzkriterien zuordnen; keine erfüllten Kriterien aus einem
  grünen Formatter oder einem Testlauf ohne ausgeführte Tests ableiten.
- Fehler der Umgebung von vorhandenen Repository-Defekten und neuen Fehlern trennen.
  Keine Prüfungen deaktivieren oder Assertions abschwächen, um Erfolg zu melden.
- Zusätzliche Defekte außerhalb des Issues separat als Befund notieren. Dafür weder
  weitere Issues veröffentlichen noch unaufgefordert zusätzliche Features bauen.
- PR-Beschreibung aus dem finalen Diff schreiben: konkretes Problem, resultierendes
  Verhalten, Validierung und verbleibende Grenzen. Keine unnötige Ablaufchronik.
- Bei fehlendem GitHub-Zugriff einen lokalen PR-Entwurf liefern und genau benennen,
  welche Remote-Aktion nicht möglich war. Keine Veröffentlichung behaupten.
