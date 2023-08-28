import csv
import pprint
import re

import requests
import requests_cache

import geopandas as gpd
from shapely.geometry import Point

requests_cache.install_cache('http_cache', backend='sqlite', expire_after=1800)  # 1800 seconds = 30 minutes


def get_us_state(latitude, longitude, gdf):
    # Load the shapefile into a GeoDataFrame
    # gdf = gpd.read_file(us_state_shapefile_path)

    # Create a Point object for the given latitude and longitude
    point = Point(longitude, latitude)

    # Find the state that contains the point
    state_name = None
    for index, state_row in gdf.iterrows():
        if state_row['geometry'].contains(point):
            state_name = state_row['STATE']
            break

    return state_name


def get_nation(latitude, longitude, gdf):
    point = Point(longitude, latitude)

    country_name = None
    for index, country_row in gdf.iterrows():
        if country_row['geometry'].contains(point):
            country_name = country_row['COUNTRY']
            break

    return country_name


us_state_shapefile_path = '../../../s_08mr23/s_08mr23.shp'
us_state_gdf = gpd.read_file(us_state_shapefile_path)

world_shapefile_path = '../../../World_Countries_Generalized/World_Countries_Generalized.shp'
world_gdf = gpd.read_file(world_shapefile_path)


def read_csv_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dict_list = []
        for row in reader:
            dict_list.append(row)
        return dict_list


def save_list_of_dicts_to_tsv(list_of_dicts, filename):
    """Saves a list of dicts to a TSV file.

    Args:
      list_of_dicts: A list of dicts to save.
      filename: The filename of the TSV file to save to.
    """

    with open(filename, "w") as tsvfile:
        writer = csv.DictWriter(tsvfile, fieldnames=list_of_dicts[0].keys())
        writer.writeheader()
        for dict in list_of_dicts:
            writer.writerow(dict)


def extract_lat_long(input_string):
    # Regular expression to extract latitude and longitude from three possible formats
    pattern1 = r'([-+]?\d+(?:\.\d+)?)\s*([NS])\s*:\s*([-+]?\d+(?:\.\d+)?)\s*([EW])'
    pattern2 = r'\(([NS]):([EW])\)\s*([-+]?\d+(?:\.\d+)?)\s*:\s*([-+]?\d+(?:\.\d+)?)'
    pattern3 = r'([-+]?\d+(?:\.\d+)?)\s*([NS])\s+([-+]?\d+(?:\.\d+)?)\s*([EW])'

    match1 = re.search(pattern1, input_string)
    match2 = re.search(pattern2, input_string)
    match3 = re.search(pattern3, input_string)

    if match1:
        latitude = float(match1.group(1))
        longitude = float(match1.group(3))

        if match1.group(2).upper() == 'S':
            latitude = -latitude

        if match1.group(4).upper() == 'W':
            longitude = -longitude

        return latitude, longitude

    elif match2:
        latitude = float(match2.group(3))
        longitude = float(match2.group(4))

        if match2.group(1).upper() == 'S':
            latitude = -latitude

        if match2.group(2).upper() == 'W':
            longitude = -longitude

        return latitude, longitude

    elif match3:
        latitude = float(match3.group(1))
        longitude = float(match3.group(3))

        if match3.group(2).upper() == 'S':
            latitude = -latitude

        if match3.group(4).upper() == 'W':
            longitude = -longitude

        return latitude, longitude
    else:
        # print(f"Can't extract latitude and longitude from string: {input_string}")
        return None, None


def reverse_geocode(latitude, longitude):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        # "result_type": "country|administrative_area_level_1|administrative_area_level_2|colloquial_area|locality|sublocality|neighborhood",
        "result_type": "administrative_area_level_1",
        "key": "AIzaSyAYiqbsxe6sG1Nys1nDWGARxhxVUcvAw9A"
    }

    response = requests.get(base_url, params=params)

    # Check if the response came from the cache
    if getattr(response, 'from_cache', False):
        print("The response came from the cache.")
    else:
        print("The response was not cached.")

    data = response.json()

    if data["status"] == "OK" and len(data["results"]) > 0:
        return data["results"]
    else:
        pprint.pprint(f"Can't reverse geocode {latitude},{longitude}")


ncbi_lat_lon_summary = read_csv_file("/home/mark/non_attribute_metadata_harmonized_wide_202307242110.csv")

sorted_list_by_gln = sorted(ncbi_lat_lon_summary, key=lambda x: x['geo_loc_name'])

# pprint.pprint(ncbi_lat_lon_summary[0:9])
lat_lons_only = [x["lat_lon"] for x in ncbi_lat_lon_summary]
lat_lons_only = list(set(lat_lons_only))
# lat_lons_only.sort()

# lat_lons_only = [
#     "40.05 N 75.215 W"
# ]

# https://developers.google.com/maps/documentation/places/web-service/supported_types

results_rows = []

for row in sorted_list_by_gln:
    pprint.pprint(row)
    state = None
    nation = None
    lat_element = None
    lon_element = None
    lat, lon = extract_lat_long(row['lat_lon'])
    if lat and lon:
        lat_element = lat
        lon_element = lon
        state_result = get_us_state(lat, lon, us_state_gdf)
        nation_result = get_nation(lat, lon, world_gdf)
        if state_result:
            state = state_result
        if nation_result:
            nation = nation_result
        # print(f"{row['lat_lon'] = } is in {state}")
    result_dict = {
        "geo_loc_name": row['geo_loc_name'],
        "raw_lat_lon": row['lat_lon'],
        "lat": lat_element,
        "lon": lon_element,
        "nation": nation,
        "state": state
    }

    pprint.pprint(result_dict)

    results_rows.append(result_dict)

# for ncbi_lat_lon in lat_lons_only:
#     lat, lon = extract_lat_long(ncbi_lat_lon)
#     if lat and lon:
#         state = get_us_state(lat, lon, us_state_gdf)
#         if state:
#             print(f"{ncbi_lat_lon = } is in {state}")
#             results_rows.append({"lat_lon": ncbi_lat_lon, "state": state})
#         else:
#             print(f"{ncbi_lat_lon = } is not in a state")
#             # from_google = reverse_geocode(lat, lon)
#         # if from_google:
#         #     # pprint.pprint(from_google)
#         #     a_c = from_google[0]['address_components']
#         #     g_lat = from_google[0]['geometry']['location']['lat']
#         #     g_lon = from_google[0]['geometry']['location']['lng']
#         #     country = "UNKONWN"
#         #     admin1 = "UNKONWN"
#         #     locality = "UNKONWN"
#         #     for i in a_c:
#         #         if "country" in i['types']:
#         #             country = i['long_name']
#         #         if "administrative_area_level_1" in i['types']:
#         #             admin1 = i['long_name']
#         #         if "locality" in i['types']:
#         #             locality = i['long_name']
#         #     assembled = f"{country}: {admin1}, {locality}"
#         #     print(f"{ncbi_lat_lon = } {assembled = }")
#         #     # results_rows.append({"lat_lon": ncbi_lat_lon, "assembled": assembled})
#         #     results_dict = {
#         #         "raw_lat_lon": ncbi_lat_lon,
#         #         "extracted_lat": f"{lat}",
#         #         "extracted_lon": f"{lon}",
#         #         "google_centroid_lat": f"{g_lat}",
#         #         "google_centroid_lon": f"{g_lon}",
#         #         "country": country,
#         #         "admin1": admin1,
#         #         "locality": locality,
#         #         "assembled": assembled
#         #     }
#         #     results_rows.append(results_dict)

pprint.pprint(results_rows)

save_list_of_dicts_to_tsv(results_rows, "results.tsv")

# # Make a request (this will be cached)
# response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
#
# # Check if the response came from the cache
# if getattr(response, 'from_cache', False):
#     print("The response came from the cache.")
# else:
#     print("The response was not cached.")
#
# # Make the same request again (this should come from the cache)
# response_cached = requests.get('https://jsonplaceholder.typicode.com/todos/1')
#
# # Check if the response came from the cache
# if getattr(response_cached, 'from_cache', False):
#     print("The response came from the cache.")
# else:
#     print("The response was not cached.")
