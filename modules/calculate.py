from skyfield.api import load
from entity.signs import Signs


class Calculate:
    planets = load('de421.bsp')  # Carga de efemérides
    ts = load.timescale()  # Carga de la escala de tiempo

    @staticmethod
    def calculate_planet_position(planet_name, date):
        # Convierte la fecha a la escala de tiempo de Skyfield
        t = Calculate.ts.utc(date.year, date.month, date.day)

        # Calcula la posición del planeta
        astrometric = Calculate.planets['earth'].at(t).observe(Calculate.planets[planet_name])
        _, ecliptic_lon, _ = astrometric.ecliptic_latlon()

        return ecliptic_lon.degrees

    @staticmethod
    def adjust_longitudes(longitudes):
        """
        Ajusta una lista de longitudes para evitar saltos de discontinuidad
        (por ejemplo, de 359° a 1°).
        """
        if not longitudes:
            return []

        adjusted = [longitudes[0]]
        offset = 0
        for i in range(1, len(longitudes)):
            prev = longitudes[i-1]
            curr = longitudes[i]

            # Detecta un salto de 360 a 0
            if prev - curr > 180:
                offset += 360
            # Detecta un salto de 0 a 360 (movimiento retrógrado)
            elif curr - prev > 180:
                offset -= 360

            adjusted.append(curr + offset)

        return adjusted

    @staticmethod
    def calculate_zodiac_sign(degree):
        # Obtiene el signo zodiacal dividiendo el grado por 30
        index = int(degree // 30)
        return Signs.ZODIAC[index]

    @staticmethod
    def sign_to_value(sign):
        # Convierte el signo zodiacal a su índice numérico
        return Signs.ZODIAC.index(sign)
