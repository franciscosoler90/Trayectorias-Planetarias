# Trayectorias Planetarias

Una herramienta astronómica en Python para calcular y visualizar las trayectorias eclípticas de Plutón, Urano y Neptuno utilizando la librería `skyfield`.

## Descripción General

Este proyecto ofrece una implementación moderna para rastrear las posiciones de los planetas en el sistema solar. Utiliza `skyfield`, el sucesor de la clásica librería `ephem`, para calcular la longitud eclíptica de Plutón, Urano y Neptuno.

El objetivo principal es proporcionar una herramienta educativa y robusta para entender el movimiento planetario, evitando problemas comunes de instalación de dependencias complejas.

## Características

- **Cálculo de Posición Planetaria**: Utiliza `skyfield` para obtener la longitud eclíptica de los planetas con alta precisión.
- **Visualización Gráfica**: Genera un gráfico con `matplotlib` que muestra las trayectorias de los planetas.
- **Manejo de Discontinuidades**: Incluye una función para ajustar los valores de longitud y evitar saltos abruptos (de 360° a 0°), asegurando una visualización continua.
- **Código Modular y Moderno**: La lógica de cálculo está separada de la presentación, y el proyecto utiliza dependencias actuales que son fáciles de instalar en cualquier sistema.

## Empezando

Sigue estas instrucciones para obtener una copia del proyecto y ejecutarlo en tu máquina local.

### Prerrequisitos

Asegúrate de tener Python 3.x instalado en tu sistema.

### Instalación y Ejecución

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/fransolerc/Trayectorias-Planetarias.git
    cd Trayectorias-Planetarias
    ```

2.  **Crea y activa un entorno virtual (recomendado):**
    ```bash
    python -m venv env
    # En Windows
    .\env\Scripts\activate
    # En macOS/Linux
    source env/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    `skyfield` descarga automáticamente los datos de efemérides necesarios la primera vez que se ejecuta.

4.  **Ejecuta el script principal:**
    ```bash
    python main.py
    ```
    Al ejecutarlo, se mostrará un gráfico con las trayectorias planetarias para el año 2024.

## Uso

Para cambiar el período de tiempo de la simulación, puedes modificar las variables `start_date` y `end_date` en el archivo `main.py`.

```python
# main.py
def main():
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)
    # ...
```

## Estructura del Proyecto

```
.
├── entity/
│   └── signs.py       # Define entidades (actualmente, signos del zodiaco).
├── modules/
│   └── calculate.py   # Contiene la lógica para los cálculos astronómicos con skyfield.
├── main.py            # Script principal que ejecuta la simulación y genera el gráfico.
├── requirements.txt   # Lista de dependencias de Python.
└── README.md          # Este archivo.
```

## Dependencias

-   `skyfield`: Para los cálculos de mecánica celeste.
-   `matplotlib`: Para la generación de gráficos.

## Contribuciones

Este proyecto fue creado con fines educativos. Las contribuciones que mejoren la funcionalidad, la documentación o la estructura del código son bienvenidas. Si tienes alguna sugerencia, por favor abre un *issue* o envía un *pull request*.
