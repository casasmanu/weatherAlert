import schedule
import time
import pronosticos
from drvTelegram import bot_send_msg, getNewUsers

def main():
    api_key = "bdf76432f098462e23b85ad0171ccf90"
    city = "munich"

    if not api_key or not city:
        print("Asegúrate de configurar las variables de entorno OPENWEATHERMAP_API_KEY y OPENWEATHERMAP_CITY.")
        return

    # Programa las llamadas a las funciones en intervalos diferentes
    #schedule.every(1).hour.do(pronosticos.obtener_pronostico_actual, api_key=api_key, city=city)
    #schedule.every(3).hours.do(pronosticos.obtener_pronostico_corto_plazo, api_key=api_key, city=city)
    #schedule.every().day.at("09:05").do(pronosticos.obtener_pronostico_largo_plazo, api_key=api_key, city=city)
    outputPronostico=pronosticos.obtener_pronostico_actual(api_key=api_key,city=city)

    bot_send_msg("6442113046:AAEve1WZCEp16oIVsX6XLeLfiCopymnkwtk",5178063489,outputPronostico)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()
