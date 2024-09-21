import ephem
from entity.signs import Signs


class Calculate:

    @staticmethod
    def calculate_zodiac_sign(degree):
        # Get the zodiac sign by dividing the degree by 30
        index = int(degree // 30)
        return Signs.ZODIAC[index]

    @staticmethod
    def calculate_planet_position(planet, date):
        # Set up the observer for the given date
        observer = ephem.Observer()
        observer.date = date
        planet.compute(observer)

        # Get the ecliptic longitude of the planet and convert it to degrees
        ecliptic_longitude = float(planet.hlong) * 180.0 / ephem.pi
        ecliptic_longitude = ecliptic_longitude % 360
        return ecliptic_longitude

    @staticmethod
    def sign_to_value(sign):
        # Convert the zodiac sign to its numerical index in the list
        return Signs.ZODIAC.index(sign)

    def compute(self, observer):
        # Implement any additional computation logic here
        pass
