import ephem
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from modules.calculate import Calculate


def adjust_longitudes(longitudes):
    adjusted_longitudes = []
    previous_value = None

    for longitude in longitudes:
        if previous_value is not None and previous_value - longitude > 300:
            # If there's a large jump (i.e., from ~360° to ~0°), adjust by adding 360° to the current longitude
            adjusted_longitudes.append(longitude + 360)
        else:
            adjusted_longitudes.append(longitude)

        previous_value = longitude

    return adjusted_longitudes


def main():
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)

    dates = []
    pluto_longitudes = []
    uranus_longitudes = []
    neptune_longitudes = []

    delta = datetime.timedelta(days=10)  # Interval of 10 days
    current_date = start_date
    while current_date < end_date:
        # Calculate the ecliptic longitude of Pluto in degrees
        pluto_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Pluto(), current_date)
        pluto_longitudes.append(pluto_ecliptic_longitude)

        # Calculate the ecliptic longitude of Uranus in degrees
        uranus_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Uranus(), current_date)
        uranus_longitudes.append(uranus_ecliptic_longitude)

        # Calculate the ecliptic longitude of Neptune in degrees
        neptune_ecliptic_longitude = Calculate.calculate_planet_position(ephem.Neptune(), current_date)
        neptune_longitudes.append(neptune_ecliptic_longitude)

        dates.append(current_date)
        current_date += delta

    # Adjust the longitudes to avoid jumps from 360° to 0°
    pluto_longitudes = adjust_longitudes(pluto_longitudes)
    uranus_longitudes = adjust_longitudes(uranus_longitudes)
    neptune_longitudes = adjust_longitudes(neptune_longitudes)

    # Convert the dates to numerical format for matplotlib
    dates_num = mdates.date2num(dates)

    plt.figure(figsize=(10, 6))

    # Plot the adjusted ecliptic longitude values for each planet
    plt.plot(dates_num, pluto_longitudes, label='Pluto', linestyle='-', marker='o')
    plt.plot(dates_num, uranus_longitudes, label='Uranus', linestyle='-', marker='o')
    plt.plot(dates_num, neptune_longitudes, label='Neptune', linestyle='-', marker='o')

    plt.xlabel('Date')
    plt.ylabel('Ecliptic Longitude (Degrees)')
    plt.title('Ecliptic Longitudes of Pluto, Uranus, and Neptune (0° to 360°)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Invert the Y-axis so that 0° is at the bottom and 360° at the top
    plt.gca().invert_yaxis()

    # Format the X-axis with dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format as Year-Month-Day
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # Major ticks every year

    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
