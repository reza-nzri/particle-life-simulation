# Contributing Guidelines

Dieses Dokument beschreibt die Coding Conventions und Entwicklungsregeln für das Projekt **Particle Life Simulation**.

## 1. Sprache und Dokumentation

- **Code:** Englische Namen für Variablen, Funktionen, Klassen und Module.
- **Kommentare:** Einfaches, verständliches Deutsch.
- **Docstrings:** Einfaches Deutsch.
- **Dokumentation:** Deutsch, einschließlich README und Markdown-Dateien.
- **Commit-Messages:** Englisch.

Jede Funktion erhält einen kurzen Docstring, der ihren Zweck sowie **Input (Parameter)** und **Output (Rückgabewert)** beschreibt. Bei Funktionen ohne Rückgabewert wird dies entsprechend angegeben.

Kommentare sollen erklären, *warum* etwas gemacht wird, nicht jede offensichtliche Codezeile wiederholen.

## 2. Naming Conventions

| Element | Konvention | Beispiel |
|---|---|---|
| Variablen | `snake_case` | `first_name`, `total_count` |
| Funktionen | `snake_case` | `calculate_average()` |
| Konstanten | `UPPER_SNAKE_CASE` | `MAX_SPEED = 100` |
| Klassen | `PascalCase` | `ParticleSimulation` |
| Module/Dateien | `snake_case` | `particle_system.py` |
| Private Variablen | `_snake_case` | `_internal_value` |

Die Benennung orientiert sich an [PEP 8](https://peps.python.org/pep-0008/). Namen sollen eindeutig und verständlich sein.

## 3. Python Coding Conventions

- **PEP 8:** Einheitlicher Python-Code-Stil.
- **Type Hints:** Parameter und Rückgabewerte typisieren.
- **PEP 257:** Docstrings für Funktionen, Klassen und Module verwenden.
- **DRY:** Unnötige Code-Duplikate vermeiden.
- **KISS:** Einfache und verständliche Lösungen bevorzugen.
- **Single Responsibility:** Funktionen und Klassen sollen klar abgegrenzte Aufgaben erfüllen.
- **Imports:** Standardbibliothek, externe Pakete und lokale Module getrennt importieren.
- **Fehlerbehandlung:** Konkrete Exceptions verwenden und Fehler nicht stillschweigend ignorieren.
- **Dependencies:** Nur benötigte Pakete hinzufügen und mit `uv` verwalten.

## 4. Projektarchitektur

- Simulationslogik und Visualisierung bleiben getrennt.
- Die Simulationslogik muss ohne grafische Oberfläche ausführbar und testbar sein.
- Konfigurationsparameter werden zentral verwaltet.
- Neue Module sollen eine eindeutige Aufgabe erfüllen.
- Architekturänderungen werden in [docs/architecture.md](docs/architecture.md) dokumentiert.

## 5. Tests und Codequalität

Für neue Funktionen und Fehlerbehebungen sollen passende Tests geschrieben werden.

**Tests ausführen:**

```powershell
uv run pytest
```

**Code prüfen:**

```powershell
uv run ruff check .
```

**Formatierung überprüfen:**

```powershell
uv run ruff format --check .
```

**Code formatieren:**

```powershell
uv run ruff format .
```

**Testabdeckung messen:**

```powershell
uv run pytest --cov=particle_life_simulation --cov-report=term-missing
```

Für die Kernlogik der Simulation wird eine Testabdeckung von mindestens **70 %** angestrebt.

## 6. Git Workflow

- Änderungen auf eigenen Feature Branches entwickeln.
- Kleine, thematisch zusammengehörige Commits erstellen.
- Vor einem Pull Request Tests und Codeprüfungen ausführen.
- Pull Requests vor dem Merge überprüfen.
- Keine unnötigen oder automatisch generierten Dateien committen.

## 7. Conventional Commits

**Format:** `type(scope): kurze Beschreibung`

| Type | Bedeutung | Beispiel |
|---|---|---|
| `feat` | Neue Funktion | `feat: add particle movement` |
| `fix` | Fehlerbehebung | `fix: correct particle velocity` |
| `docs` | Dokumentation | `docs: update README` |
| `refactor` | Code verbessern, ohne Verhalten zu ändern | `refactor: simplify force calculation` |
| `test` | Tests hinzufügen oder ändern | `test: add simulation tests` |
| `chore` | Projektverwaltung und Wartung | `chore: initialize project` |
| `ci` | CI/CD-Konfiguration | `ci: add GitHub Actions workflow` |
| `build` | Build-System und Dependencies | `build: add numpy dependency` |
| `perf` | Performance verbessern | `perf: optimize particle interactions` |
| `style` | Formatierung ohne Logikänderung | `style: format Python files` |

**Beispiel mit Scope:**

`feat(simulation): implement particle attraction`

- `feat` = Art der Änderung
- `simulation` = betroffener Projektbereich (optional)
- `implement particle attraction` = kurze Beschreibung

**Empfehlung:** Commit-Messages auf Englisch und im Imperativ schreiben. So bleibt die Git-History einheitlich.

## 8. Pull Requests

Ein Pull Request sollte:

- Eine klare Beschreibung der Änderung enthalten.
- Auf ein zugehöriges Issue verweisen, falls vorhanden.
- Nur zusammengehörige Änderungen enthalten.
- Erfolgreiche Tests und Codeprüfungen vorweisen.
- Bei Bedarf die Dokumentation aktualisieren.

## 9. Referenzen

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
