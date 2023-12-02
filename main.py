import pandas as pd
from API_data.get_API_data import get_weather
from longtude_data.longtude import dict_append
import json
import sys
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d_%m_%Y %H_%M_%S")


def check_api(api_str: dict):

    if 'message' in api_str:
        return False
    else:
        return True


df_city = pd.read_csv('longtude_data/capital_coordinates.csv', sep=',')

output_data = {}
for index, row in df_city.iterrows():

    city_name = row['City']
    place_id = row['place_id']
    latitude = row['Latitude']
    longtude = row['Longitude']

    weather = get_weather(latitude= latitude, longitude=longtude)
    bool_value = check_api(weather)

    if bool_value:
        country_name = weather['location']['country']
        localtime = weather['location']['localtime']
        tz_id = weather['location']['tz_id']


        last_updated = weather['current']['last_updated']
        temp_c = weather['current']['temp_c']
        is_day = weather['current']['is_day']
        wind_kph = weather['current']['wind_kph']
        wind_dir = weather['current']['wind_dir']
        pressure_mb = weather['current']['pressure_mb']
        humidity = weather['current']['humidity']
        feelslike_c = weather['current']['feelslike_c']
        uv = weather['current']['uv']

        jsondata = str(weather)

        dict_append(output_data, key='City', val=city_name)
        dict_append(output_data, key='latitude', val=latitude)
        dict_append(output_data, key='longtude', val=longtude)
        dict_append(output_data, key='place_id', val=place_id)

        dict_append(output_data, key='country_name', val=country_name)
        dict_append(output_data, key='localtime', val=localtime)
        dict_append(output_data, key='tz_id', val=tz_id)
        dict_append(output_data, key='last_updated', val=last_updated)
        dict_append(output_data, key='temp_c', val=temp_c)
        dict_append(output_data, key='is_day', val=is_day)
        dict_append(output_data, key='wind_kph', val=wind_kph)
        dict_append(output_data, key='wind_dir', val=wind_dir)
        dict_append(output_data, key='pressure_mb', val=pressure_mb)
        dict_append(output_data, key='humidity', val=humidity)
        dict_append(output_data, key='feelslike_c', val=feelslike_c)
        dict_append(output_data, key='uv', val=uv)
        dict_append(output_data, key='jsondata', val=jsondata)
    
    else:
        sys.exit(weather['message'])



dataframe = pd.DataFrame(output_data)
#part1.to_excel(f'API_data/part_API.xlsx', index=False)
#dataframe = pd.concat([df_city, part1])

dataframe.to_excel(f'API_data/weahter_data/full_weather {dt_string}.xlsx', index=False)






