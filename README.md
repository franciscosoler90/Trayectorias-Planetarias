# AstroZodiac: Trayectorias Planetarias en el Zodíaco (1990-2030)

Este proyecto es una herramienta astrológica desarrollada en Python que calcula y visualiza la trayectoria de Plutón, Urano y Neptuno a través de los signos zodiacales desde 1990 hasta 2030. Utiliza la librería `ephem` para calcular la posición de los planetas en fechas específicas y `matplotlib` para graficar los resultados.

## Descripción

El objetivo de este proyecto es estudiar cómo se mueven Plutón, Urano y Neptuno a lo largo de los signos del zodíaco durante un periodo de 40 años. El programa:
1. Calcula la longitud eclíptica de cada planeta para cada fecha en un intervalo de 10 días.
2. Asigna el signo zodiacal correspondiente a la posición calculada.
3. Genera un gráfico que muestra la trayectoria de cada planeta a través de los signos zodiacales.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/astrozodiac.git
   cd astrozodiac
