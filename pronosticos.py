import requests
from datetime import datetime
import json

def obtener_pronostico_actual(api_key, city):
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&units=metric&appid={api_key}"
    response = requests.get(current_url)
    data = response.json()
    ### data to extract!

    pronDesc=data['weather'][0]['description']
    pronGral=data['weather'][0]['main']
    pronTempAct=data['main']['temp']
    pronTempSens=data['main']['feels_like']
    pronTempMax=data['main']['temp_max']
    pronTempMin=data['main']['temp_min']
    pronTempHum=data['main']['humidity']
    pronTempPres=data['main']['pressure']
    pronWind=data['wind']['speed']
    pronSunset=data['sys']['sunset']
    pronSunrise=data['sys']['sunrise']
    pronTimeStamp=data['dt']

    textDateFromTimeStapm= str(datetime.fromtimestamp(pronTimeStamp))
    textSunsetTime=str(datetime.fromtimestamp(pronSunset))
    textSunriseTime=str(datetime.fromtimestamp(pronTimeStamp))

    output_text=f"{textDateFromTimeStapm} \n \
        Pronóstico Actual:{pronDesc} , {pronGral}\n \
        la temperatura es de {pronTempAct}°C y la sensacion termica {pronTempSens}°C \n \
        maxima y minima pronosticadas para hoy {pronTempMax,pronTempMin} °C \n \
        humedad %{pronTempHum} y presion {pronTempPres} Hpa \n \
        Viento: {pronWind} nudos? \n \
        hora de salida {textSunriseTime} puesta del sol {textSunsetTime}" 
    
    print(output_text)
    ## data['weather'][0]['description']
    ## data['main']['temp']
    ## data['main']['feels_like']
    #print(data)
    return output_text

obtener_pronostico_actual(api_key="bdf76432f098462e23b85ad0171ccf90",city="munich")