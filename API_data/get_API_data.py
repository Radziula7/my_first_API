import requests


def get_weather(latitude: str, longitude: str):

    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    # Latitude and Longitude 
    querystring = {"q":f"{latitude},{longitude}"}

    headers = {
    "X-RapidAPI-Key": "8a6b4c7436msh1f22f17fbff282cp15fdb4jsncf2b9220b69d",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()