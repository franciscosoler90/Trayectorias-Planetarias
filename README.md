# Planetary Trajectories

A Python astronomical tool to calculate and visualize the ecliptic trajectories of Pluto, Uranus, and Neptune using the `skyfield` library.

## Overview

This project offers a modern implementation to track the positions of planets in the solar system. It uses `skyfield`, the successor to the classic `ephem` library, to calculate the ecliptic longitude of Pluto, Uranus, and Neptune.

The main goal is to provide an educational and robust tool to understand planetary motion, avoiding common installation problems of complex dependencies.

## Features

- **Planetary Position Calculation**: Uses `skyfield` to obtain the ecliptic longitude of planets with high precision.
- **Graphical Visualization**: Generates a chart with `matplotlib` showing the trajectories of the planets.
- **Discontinuity Handling**: Includes a function to adjust longitude values and avoid abrupt jumps (from 360° to 0°), ensuring continuous visualization.
- **Modular and Modern Code**: Calculation logic is separated from presentation, and the project uses current dependencies that are easy to install on any system.
- **Command Line Interface**: Easily configure the simulation period via command line arguments.

## Getting Started

Follow these instructions to get a copy of the project and run it on your local machine.

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation and Execution

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/fransolerc/Trayectorias-Planetarias.git
    cd Trayectorias-Planetarias
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

    > **Note for Windows Users:** If you encounter the error:
    > ```
    > .\env\Scripts\activate : No se puede cargar el archivo ... porque la ejecución de scripts está deshabilitada en este sistema.
    > + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    > + FullyQualifiedErrorId : UnauthorizedAccess
    > ```
    > You need to enable script execution by running the following command in PowerShell:
    > ```powershell
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    `skyfield` automatically downloads the necessary ephemeris data the first time it runs.

4.  **Run the main script:**
    ```bash
    python main.py
    ```
    When executed, a chart showing the planetary trajectories for the year 2024 will be displayed.

## Usage

You can customize the simulation period using command-line arguments:

```bash
# Run for a specific year range
python main.py --start-date 2025-01-01 --end-date 2025-12-31
```

If no arguments are provided, it defaults to the year 2024.

## Testing

To run the unit tests, execute the following command from the project root:

```bash
python -m unittest discover tests
```

## Project Structure

```
.
├── entity/
│   └── signs.py       # Defines entities (currently, zodiac signs).
├── modules/
│   └── calculate.py   # Contains logic for astronomical calculations with skyfield.
├── tests/
│   └── test_calculate.py # Unit tests for calculation logic.
├── main.py            # Main script that runs the simulation and generates the chart.
├── requirements.txt   # List of Python dependencies.
└── README.md          # This file.
```

## Dependencies

-   `skyfield`: For celestial mechanics calculations.
-   `matplotlib`: For chart generation.

## Contributions

This project was created for educational purposes. Contributions that improve functionality, documentation, or code structure are welcome. If you have any suggestions, please open an *issue* or send a *pull request*.
