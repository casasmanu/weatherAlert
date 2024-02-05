import os
import schedule
import time
import pronosticos

def main():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    city = os.environ.get("OPENWEATHERMAP_CITY")

    if not api_key or not city:
        print("Asegúrate de configurar las variables de entorno OPENWEATHERMAP_API_KEY y OPENWEATHERMAP_CITY.")
        return

    # Programa las llamadas a las funciones en intervalos diferentes
    schedule.every(1).hour.do(obtener_pronostico_actual, api_key=api_key, city=city)
    schedule.every(3).hours.do(obtener_pronostico_corto_plazo, api_key=api_key, city=city)
    schedule.every().day.at("08:00").do(obtener_pronostico_largo_plazo, api_key=api_key, city=city)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
