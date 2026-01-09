import requests

def forecast_api(lat,lon):
    url_forecast = 'https://api.open-meteo.com/v1/forecast'
    params_forecast = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,weather_code",
        "forecast_days" : 2,
        "current": "temperature_2m",
        "timezone": "auto"
        }
    
    response_forecast = requests.get(url_forecast,params=params_forecast)
    data = response_forecast.json()
    if 'hourly' not in data:
        data = None
    return data

    
