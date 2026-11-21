# Particle Life Simulation

Eine interaktive, zweidimensionale Partikelsimulation mit Python, NumPy und VisPy.

**Particle Life** simuliert das Verhalten von Partikeln, die sich abhängig von ihrem Typ und ihrer Entfernung gegenseitig anziehen oder abstoßen. Aus einfachen Interaktionsregeln entstehen dynamische Bewegungsmuster und komplexe Strukturen.

Die Anwendung kombiniert eine numerische Simulationslogik mit einer grafischen Visualisierung und ermöglicht die Untersuchung unterschiedlicher Partikelinteraktionen.

## Demo

| Simulation | Partikelinteraktionen |
|:---:|:---:|
| ![Particle Life Simulation](docs/images/simulation.png) | ![Partikelinteraktionen](docs/images/interactions.png) |
| Gesamtansicht der Simulation | Verhalten verschiedener Partikeltypen |


## Funktionen

<details>
<summary>Simulationsfunktionen anzeigen</summary>

- Zweidimensionale Partikelsimulation
- Mehrere Partikeltypen mit unterschiedlichen Eigenschaften
- Anziehung und Abstoßung zwischen Partikeln
- Konfigurierbare Interaktionsmatrix
- Einstellbare Partikelzahl und Interaktionsreichweite
- Berechnung von Positionen und Geschwindigkeiten
- Grafische Darstellung der Partikelbewegungen
- Trennung von Simulationslogik und Visualisierung

</details>

## Installation

<details>
<summary>Voraussetzungen und Installation anzeigen</summary>

**Voraussetzungen:**

- Python 3.13
- Git
- [uv](https://docs.astral.sh/uv/)

**1. Repository klonen**

```powershell
git clone https://github.com/reza-nzri/particle-life-simulation.git
cd particle-life-simulation
```

**2. Abhängigkeiten installieren**

```powershell
uv sync
```

Die benötigten Pakete werden anhand der Projektkonfiguration installiert.

</details>


## Anwendung starten

<details>
<summary>Simulation ausführen</summary>

Nach der Installation kann die Simulation gestartet werden:

```powershell
uv run python -m particle_life_simulation
```

Die Anwendung startet die Partikelsimulation und zeigt die Bewegungen und Wechselwirkungen der Partikel grafisch an.

</details>


## Technologie-Stack

<details>
<summary>Verwendete Technologien anzeigen</summary>

| Technologie | Verwendung |
|---|---|
| Python | Programmiersprache |
| NumPy | Numerische Berechnungen |
| VisPy | Grafische Visualisierung |
| uv | Paket- und Projektverwaltung |
| pytest | Automatisierte Tests |
| pytest-cov | Messung der Testabdeckung |
| Ruff | Linting und Formatierung |
| GitHub Actions | Continuous Integration |

</details>

## Projektstruktur

<details>
<summary>Verzeichnisstruktur und Dateibeschreibungen anzeigen</summary>

```text
particle-life-simulation/
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # Automatische Tests und Codeprüfungen
│
├── src/
│   └── particle_life_simulation/
│       ├── __init__.py            # Kennzeichnet das Python-Paket
│       ├── py.typed               # Kennzeichnet das Paket als typisiert
│       ├── config.py              # Konfiguration der Simulationsparameter
│       ├── simulation.py          # Berechnung der Partikelbewegungen
│       └── visualization.py       # Grafische Darstellung der Simulation
│
├── tests/
│   ├── test_config.py             # Tests der Konfiguration
│   └── test_simulation.py         # Tests der Simulationslogik
│
├── benchmarks/
│   └── benchmark_simulation.py    # Messung der Simulationsleistung
│
├── docs/
│   ├── images/                    # Bilder und Screenshots
│   │   ├── simulation.png         # Gesamtansicht der Simulation
│   │   └── interactions.png       # Darstellung der Partikelinteraktionen
│   └── architecture.md            # Beschreibung der Softwarearchitektur
│
├── .gitignore                     # Von Git ausgeschlossene Dateien
├── .python-version                # Verwendete Python-Version
├── pyproject.toml                 # Projektkonfiguration und Abhängigkeiten
├── uv.lock                        # Festgelegte Paketversionen
└── README.md                      # Projektübersicht und Dokumentation
```

Die Simulationslogik ist unabhängig von der Visualisierung aufgebaut. Dadurch können Berechnungen separat getestet und ihre Leistung gemessen werden.

</details>

## Qualitätssicherung

<details>
<summary>Tests, Codeprüfung und Formatierung anzeigen</summary>

**Tests ausführen**

```powershell
uv run pytest
```

**Code mit Ruff prüfen**

```powershell
uv run ruff check .
```

**Formatierung überprüfen**

```powershell
uv run ruff format --check .
```

**Code automatisch formatieren**

```powershell
uv run ruff format .
```

**Testabdeckung messen**

```powershell
uv run pytest --cov=particle_life_simulation --cov-report=term-missing
```

Die automatisierten Tests überprüfen insbesondere die Kernlogik der Simulation.

Weitere Informationen zu Entwicklung, Tests und Coding Conventions stehen in [CONTRIBUTING.md](CONTRIBUTING.md).

</details>

## Architektur

<details>
<summary>Aufbau der Anwendung anzeigen</summary>

Die Anwendung ist in drei zentrale Bereiche unterteilt:

**1. Konfiguration (`config.py`)**

Verwaltet die Parameter der Simulation, beispielsweise Partikelzahl, Partikeltypen und Interaktionsregeln.

**2. Simulation (`simulation.py`)**

Berechnet die Wechselwirkungen zwischen Partikeln und aktualisiert ihre Positionen und Geschwindigkeiten.

**3. Visualisierung (`visualization.py`)**

Stellt die berechneten Partikelzustände grafisch dar.

Weitere Informationen befinden sich in [docs/architecture.md](docs/architecture.md).

</details>
