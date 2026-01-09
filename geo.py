import requests

#pega a cidade e busca a latitude e longitude
def geo_api(city):
    url_geo = 'https://geocoding-api.open-meteo.com/v1/search'

    params_geo = {
        'name' : city,
        'count' : 1,
        'language' : 'pt',
    }

    response_geo = requests.get(url_geo, params=params_geo)
    data = response_geo.json()
    
    if 'results' not in data:
        return None
    
    return data['results'][0] 

#pega a latitude e longitude e verifica a temperatura
# def weather_api(lat, lon):
#     url_temp = 'https://api.open-meteo.com/v1/forecast'

#     params_temp = {
#         "latitude": lat,
#         "longitude": lon,
#         "current": "temperature_2m",
#         "timezone": "auto"
#     }

#     response_temp = requests.get(url_temp,params=params_temp)
#     data = response_temp.json()
    
#     if "current" not in data:
#         return None
#     return data['current']['temperature_2m']

