import ephem
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius",
                "Capricorn", "Aquarius", "Pisces"]


def calculate_zodiac_sign(degree):
    index = int(degree // 30)
    return zodiac_signs[index]


def calculate_planet_position(planet, date):
    observer = ephem.Observer()
    observer.date = date
    planet.compute(observer)

    # Get the ecliptic longitude of the planet
    ecliptic_longitude = float(planet.hlong) * 180.0 / ephem.pi
    ecliptic_longitude = ecliptic_longitude % 360
    return ecliptic_longitude


def sign_to_value(sign):
    return zodiac_signs.index(sign)


def main():
    start_date = datetime.datetime(1990, 1, 1)
    end_date = datetime.datetime(2030, 12, 31)

    dates = []
    pluto_values = []
    uranus_values = []
    neptune_values = []

    delta = datetime.timedelta(days=10)  # Interval of 10 days
    current_date = start_date
    while current_date < end_date:
        pluto_ecliptic_longitude = calculate_planet_position(ephem.Pluto(), current_date)
        pluto_sign = calculate_zodiac_sign(pluto_ecliptic_longitude)
        pluto_value = sign_to_value(pluto_sign)

        uranus_ecliptic_longitude = calculate_planet_position(ephem.Uranus(), current_date)
        uranus_sign = calculate_zodiac_sign(uranus_ecliptic_longitude)
        uranus_value = sign_to_value(uranus_sign)

        neptune_ecliptic_longitude = calculate_planet_position(ephem.Neptune(), current_date)
        neptune_sign = calculate_zodiac_sign(neptune_ecliptic_longitude)
        neptune_value = sign_to_value(neptune_sign)

        dates.append(current_date)
        pluto_values.append(pluto_value)
        uranus_values.append(uranus_value)
        neptune_values.append(neptune_value)

        current_date += delta

    # Convert the dates to numerical format for matplotlib
    dates_num = mdates.date2num(dates)

    plt.figure(figsize=(10, 6))

    plt.plot(dates_num, pluto_values, label='Pluto', linestyle='-', marker='o')
    plt.plot(dates_num, uranus_values, label='Uranus', linestyle='-', marker='o')
    plt.plot(dates_num, neptune_values, label='Neptune', linestyle='-', marker='o')

    plt.xlabel('Date')
    plt.ylabel('Zodiac Sign')
    plt.title('Path of Pluto, Uranus, and Neptune through Zodiac Signs')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Set custom labels for the Y-axis with zodiac signs
    plt.yticks(range(len(zodiac_signs)), zodiac_signs)
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
