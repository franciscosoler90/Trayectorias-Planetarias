import ephem
import datetime
import matplotlib.pyplot as plt


def calcular_signo_zodiacal(grado):
    signos_zodiacales = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario",
                         "Capricornio", "Acuario", "Piscis"]
    indice = int(grado // 30)
    return signos_zodiacales[indice]


def calcular_posicion_planeta(planeta, fecha):
    observador = ephem.Observer()
    observador.date = fecha
    planeta.compute(observador)

    try:
        # Usar la longitud heliocéntrica directamente si está disponible
        longitud_ecliptica = float(planeta.hlong) * 180.0 / ephem.pi
    except AttributeError:
        # Como alternativa, puedes calcularla manualmente o usar 'ra' y 'dec'
        longitud_ecliptica = float(planeta.ra) * 180.0 / ephem.pi

    longitud_ecliptica = longitud_ecliptica % 360
    return longitud_ecliptica


def main():
    fecha_inicial = datetime.datetime(1990, 1, 1)
    fecha_final = datetime.datetime(2030, 12, 31)

    fechas = []
    signos_pluton = []
    signos_urano = []
    signos_neptuno = []

    delta = datetime.timedelta(days=10)  # Intervalo de 10 días
    fecha_actual = fecha_inicial
    while fecha_actual < fecha_final:
        # Calcula la posición de Plutón
        longitud_ecliptica_pluton = calcular_posicion_planeta(ephem.Pluto(), fecha_actual)
        signo_pluton = calcular_signo_zodiacal(longitud_ecliptica_pluton)

        # Calcula la posición de Urano
        longitud_ecliptica_urano = calcular_posicion_planeta(ephem.Uranus(), fecha_actual)
        signo_urano = calcular_signo_zodiacal(longitud_ecliptica_urano)

        # Calcula la posición de Neptuno
        longitud_ecliptica_neptuno = calcular_posicion_planeta(ephem.Neptune(), fecha_actual)
        signo_neptuno = calcular_signo_zodiacal(longitud_ecliptica_neptuno)

        fechas.append(fecha_actual)
        signos_pluton.append(signo_pluton)
        signos_urano.append(signo_urano)
        signos_neptuno.append(signo_neptuno)

        fecha_actual += delta

    plt.figure(figsize=(10, 6))

    # Graficar la trayectoria de Plutón
    plt.plot(fechas, signos_pluton, label='Plutón', linestyle='-', marker='o')

    # Graficar la trayectoria de Urano
    plt.plot(fechas, signos_urano, label='Urano', linestyle='-', marker='o')

    # Graficar la trayectoria de Neptuno
    plt.plot(fechas, signos_neptuno, label='Neptuno', linestyle='-', marker='o')

    plt.xlabel('Fecha')
    plt.ylabel('Signo zodiacal')
    plt.title('Trayectoria de Plutón, Urano y Neptuno a través de los signos del zodíaco')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
