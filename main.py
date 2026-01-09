import requests
import time
import sys
from datetime import datetime
from geo import geo_api
from weather import forecast_api
from engine import run_engine
from rules import calor_extremo, chuva_forte, chuva, tempestade
from log import salvar_log

agora = datetime.now()
agora_fmt = agora.strftime("%d/%m/%Y %H:%M")
cidade = input('Digite o nome da cidade:')
data_geo = geo_api(cidade)

if data_geo == None:
    print('Cidade não encontrada')
    exit ()
    
nome = data_geo['name']
latitude = data_geo['latitude']
longitude = data_geo['longitude']
pais = data_geo["country"]

forecast = forecast_api(lat=latitude,lon=longitude)
data_forecast = forecast['hourly']
temp = forecast['current']['temperature_2m']


print(f"🔎 Buscando o clima de {cidade}", end="")
for _ in range(3):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)
    
print ('\n✅ Pronto!')
time.sleep(0.5)

print(f'🌤️  Neste momento em {cidade} está fazendo {temp}°C.')

alerts = []
while True:
    
    user = input(f'📅 Quer ver a previsão das próximas 48h em {cidade}? (y/n):')
    if user.lower() == 'y':
        print(f'🔍 Previsão das próximas 48h em {cidade}:')
            
        rules =[
            {"message": "🔥 Calor extremo", "check": calor_extremo},
            {"message": "🌧️ Chuva forte", "check": chuva_forte},
            {"message": "⛈️ Tempestade", "check": tempestade},
            {"message": "🌦️ Chuva", "check": chuva}
        ]

        alerts = run_engine(rules,data_forecast)

        for alert in alerts:
            print(alert)
        if not alerts:
            print(f'Clima normal para {cidade}')
        break
    elif user.lower() == 'n':
        print(f'Encerrando por aqui. Tenha um ótimo dia! ☀️')
        break
    else:
        print('⚠️ Resposta não reconhecida. Digite "y" ou "n".')
        continue
if not alerts:
    salvar_log(f'{'=' * 50} \n 🕒 {agora_fmt}\n 🌍 Nova consulta de clima iniciada\n 📌 Cidade: {cidade}\n {"=" * 50} ')
else:
    salvar_log(f'{'=' * 50} \n 🕒 {agora_fmt}\n 🌍 Nova consulta de clima iniciada\n 📌 Cidade: {cidade}\n {"-" * 50} ')
    for alert in alerts:
        salvar_log(f'🚨ALERTA:{alert}')
    salvar_log('=' * 50 )
