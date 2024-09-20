import ephem
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from modules.calculate import Calculate
from entity.signs import Signs


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
        pluto_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Pluto(), current_date)
        pluto_sign = Calculate.calculate_zodiac_sign(pluto_ecliptic_longitude)
        pluto_value = Calculate.sign_to_value(pluto_sign)

        uranus_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Uranus(), current_date)
        uranus_sign = Calculate.calculate_zodiac_sign(uranus_ecliptic_longitude)
        uranus_value = Calculate.sign_to_value(uranus_sign)

        neptune_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Neptune(), current_date)
        neptune_sign = Calculate.calculate_zodiac_sign(neptune_ecliptic_longitude)
        neptune_value = Calculate.sign_to_value(neptune_sign)

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
    plt.yticks(range(len(Signs.zodiac)), Signs.zodiac)
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
