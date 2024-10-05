# Trayectorias Planetarias

Este proyecto es una herramienta astronómica desarrollada en Python que calcula y visualiza la trayectoria de Plutón, Urano y Neptuno. Utiliza la librería `ephem` para calcular la posición de los planetas en fechas específicas y `matplotlib` para graficar los resultados.

## Descripción

El objetivo de este proyecto es estudiar cómo se mueven Plutón, Urano y Neptuno a lo largo del tiempo. 
El programa:
1. Calcula la longitud eclíptica de cada planeta para cada fecha en un intervalo de 10 días.
2. Genera un gráfico que muestra la trayectoria de cada planeta.

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/fransolerc/Trayectorias-Planetarias.git
cd Trayectorias-Planetarias
```

2. Configura un Entorno Virtual (Opcional, pero recomendado)
```bash
python -m venv env
.\env\Scripts\activate
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

4. Ejecutar el proyecto
```bash
python main.py
```

## Dependencias
Este proyecto requiere las siguientes librerías:

- ephem: Para cálculos astronómicos.
- matplotlib: Para la visualización gráfica.
- datetime: Para la gestión de fechas (incluido en la biblioteca estándar de Python).

Estas dependencias están listadas en el archivo requirements.txt.

## Resultados
El gráfico resultante muestra cómo los planetas transitan en el periodo de tiempo especificado.

## Aprendizajes
Este proyecto me ha permitido aprender sobre:

- Uso de la librería ephem para cálculos astronómicos.
- Generación y personalización de gráficos con matplotlib.
- Manejo de fechas y tiempos en Python.

## Contribuciones
Este proyecto fue realizado con fines educativos. Si tienes sugerencias o mejoras, ¡no dudes en enviar un pull request!
