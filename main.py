import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from modules.calculate import Calculate

def main():
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)

    planets_to_plot = {
        'pluto barycenter': [],
        'uranus barycenter': [],
        'neptune barycenter': []
    }
    dates = []

    # Genera las fechas
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += datetime.timedelta(days=10)

    # Calcula las posiciones para cada planeta
    for planet_name in planets_to_plot.keys():
        longitudes = [Calculate.calculate_planet_position(planet_name, date) for date in dates]
        planets_to_plot[planet_name] = Calculate.adjust_longitudes(longitudes)

    # Grafica los resultados
    plt.figure(figsize=(12, 8))
    dates_num = mdates.date2num(dates)

    for planet_name, longitudes in planets_to_plot.items():
        plt.plot(dates_num, longitudes, label=planet_name.replace(' barycenter', '').capitalize(), linestyle='-', marker='o')

    plt.xlabel('Fecha')
    plt.ylabel('Longitud Eclíptica (Grados)')
    plt.title('Longitudes Eclípticas de Plutón, Urano y Neptuno')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Formatea el eje X con fechas
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()
