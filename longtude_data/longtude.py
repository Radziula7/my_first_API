import csv
from geopy.geocoders import Nominatim
import pandas as pd

def dict_append(dictonary: dict, key: str, val) -> dict:
    if key in dictonary.keys():
        dictonary[key] += [val]
    else:
        dictonary[key] = [val]

    return dictonary


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(city_name)
    if location:
        country_name = location.address.split(",")[-1]

        place_id = location.raw["place_id"]
        latitude = location.latitude
        longitude = location.longitude
        frame = [country_name, place_id, latitude, longitude]

        return frame
    else:
        return None


def fetch_coordinates_for_capitals(capitals_file, output_file):
    with open(capitals_file, "r") as file:
        capitals = file.readlines()

    capital_coordinates = {}

    for capital in capitals:
        capital = capital.strip()
        coordinates = get_coordinates(capital)
        if coordinates:
            # capital_coordinates.append({'City': capital, 'Latitude': coordinates[0], 'Longitude': coordinates[1]})
            dict_append(dictonary=capital_coordinates, key="City", val=capital)
            dict_append(
                dictonary=capital_coordinates, key="Country", val=coordinates[-4]
            )
            dict_append(
                dictonary=capital_coordinates, key="place_id", val=coordinates[-3]
            )
            dict_append(
                dictonary=capital_coordinates, key="Latitude", val=coordinates[-2]
            )
            dict_append(
                dictonary=capital_coordinates, key="Longitude", val=coordinates[-1]
            )
    # Save coordinates to CSV

    df = pd.DataFrame(capital_coordinates)

    df.to_csv(output_file, sep=',', index=False)
    """
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["City", "Latitude", "Longitude"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in capital_coordinates:
            writer.writerow(row)
    """


if __name__ == "__main__":
    # Specify the input file containing capital city names (one city per line)
    capitals_file_path = "capital_cities.txt"

    # Specify the output CSV file
    output_file_path = "capital_coordinates.csv"

    # Fetch coordinates and save to CSV
    fetch_coordinates_for_capitals(capitals_file_path, output_file_path)
