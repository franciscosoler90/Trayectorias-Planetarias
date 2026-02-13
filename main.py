import datetime
import argparse
import logging
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from modules.calculate import Calculate

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate and visualize planetary trajectories.")
    parser.add_argument(
        '--start-date',
        type=str,
        default="2024-01-01",
        help="Start date in YYYY-MM-DD format (default: 2024-01-01)"
    )
    parser.add_argument(
        '--end-date',
        type=str,
        default="2024-12-31",
        help="End date in YYYY-MM-DD format (default: 2024-12-31)"
    )
    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d")
    except ValueError as e:
        logger.error(f"Invalid date format: {e}")
        sys.exit(1)

    if start_date > end_date:
        logger.error("Start date must be before end date.")
        sys.exit(1)

    logger.info(f"Starting simulation from {start_date.date()} to {end_date.date()}")

    planets_to_plot = [
        'pluto barycenter',
        'uranus barycenter',
        'neptune barycenter'
    ]
    dates = []

    # Generate dates
    logger.info("Generating date range...")
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += datetime.timedelta(days=10)

    # Store results for plotting
    plot_data = {}

    # Calculate positions for each planet
    logger.info("Calculating planetary positions...")
    for planet_name in planets_to_plot:
        logger.info(f"Processing {planet_name}...")
        raw_longitudes = [Calculate.calculate_planet_position(planet_name, date) for date in dates]

        # Handle discontinuities for plotting
        p_dates, p_longitudes = Calculate.handle_discontinuities(dates, raw_longitudes)
        plot_data[planet_name] = (p_dates, p_longitudes)

    # Plot results
    logger.info("Generating plot...")
    plt.figure(figsize=(12, 8))

    for planet_name, (p_dates, p_longitudes) in plot_data.items():
        dates_num = mdates.date2num(p_dates)
        plt.plot(dates_num, p_longitudes, label=planet_name.replace(' barycenter', '').capitalize(), linestyle='-', marker='o')

    plt.xlabel('Date')
    plt.ylabel('Ecliptic Longitude (Degrees)')
    plt.title('Ecliptic Longitudes of Pluto, Uranus, and Neptune')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Format X axis with dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

    plt.xticks(rotation=45)

    logger.info("Displaying plot.")
    plt.show()

if __name__ == "__main__":
    main()
