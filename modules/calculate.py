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
    def handle_discontinuities(dates, longitudes):
        """
        Inserts None values to break the plot line when a discontinuity (360 <-> 0) occurs.
        Returns new lists of dates and longitudes.
        """
        if not longitudes or not dates:
            return [], []

        new_dates = [dates[0]]
        new_longitudes = [longitudes[0]]

        for i in range(1, len(longitudes)):
            prev_lon = longitudes[i-1]
            curr_lon = longitudes[i]
            curr_date = dates[i]

            # Detect a jump greater than 180 degrees (crossing 0/360)
            if abs(curr_lon - prev_lon) > 180:
                new_dates.append(curr_date)
                new_longitudes.append(None)

            new_dates.append(curr_date)
            new_longitudes.append(curr_lon)

        return new_dates, new_longitudes

    @staticmethod
    def calculate_zodiac_sign(degree):
        # Obtiene el signo zodiacal dividiendo el grado por 30
        index = int(degree // 30)
        return Signs.ZODIAC[index]

    @staticmethod
    def sign_to_value(sign):
        # Convierte el signo zodiacal a su índice numérico
        return Signs.ZODIAC.index(sign)
