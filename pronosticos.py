import requests

def obtener_pronostico_actual(api_key, city):
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&units=metric&appid={api_key}"
    response = requests.get(current_url)
    data = response.json()
    output_text=f"Pronóstico Actual:{data['weather'][0]['description']}, la temperatura es de {data['main']['temp']}°C y la sensacion termica {data['main']['feels_like']}°C "
    print(output_text)
    ## data['weather'][0]['description']
    ## data['main']['temp']
    ## data['main']['feels_like']
    #print(data)
    return output_text

def obtener_pronostico_corto_plazo(api_key, city):
    hourly_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(hourly_url)
    data = response.json()
    print("Pronóstico a Corto Plazo (Próximas Horas):")
    print(data)

def obtener_pronostico_largo_plazo(api_key, city):
    daily_url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&appid={api_key}"
    response = requests.get(daily_url)
    data = response.json()
    print("Pronóstico a Largo Plazo (Próximos Días):")
    print(data)


