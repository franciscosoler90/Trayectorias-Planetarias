import ephem
from entity.signs import Signs


class Calculate:

    def __init__(self):
        self.Signs = None

    def calculate_zodiac_sign(degree):
        index = int(degree // 30)
        return Signs.zodiac[index]

    def calculate_planet_position(planet, date):
        observer = ephem.Observer()
        observer.date = date
        planet.compute(observer)

        # Get the ecliptic longitude of the planet
        ecliptic_longitude = float(planet.hlong) * 180.0 / ephem.pi
        ecliptic_longitude = ecliptic_longitude % 360
        return ecliptic_longitude

    def sign_to_value(sign):
        return Signs.zodiac.index(sign)

    def compute(self, observer):
        pass
