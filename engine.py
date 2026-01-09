from weather import forecast_api
from datetime import datetime

def run_engine(rules, hourly, hours=48):
    alerts = []
    now = datetime.now()  
    
    for i in range(hours):
        data, hora = hourly["time"][i].split('T')
        data = data.split('-')
        dia = data[2]
        mes = data[1]
        time_str = hourly["time"][i]
        temp = hourly['temperature_2m'][i]
        rain = hourly["precipitation"][i]
        code = hourly["weather_code"][i]
        time_obj = datetime.fromisoformat(time_str)
        if time_obj < now:
            continue  
        for rule in rules:
            if rule['check'](temp, rain, code):
                alerts.append(f'{rule["message"]} no dia {dia} do mês {mes} as {hora} ')
    return alerts       