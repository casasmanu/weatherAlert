import schedule
import time
import pronosticos
import os

from Drivers.drvTelegram import bot_send_msg, getNewUsers
from Drivers.drvConfig import readConfigFile

import Drivers.drvLogger as drvLogger

def main():
    ## INIT CONFIG
    drvLogger.initLogger()
    mainPath=os.path.abspath(os.getcwd())
    ### read config File
    config=readConfigFile(mainPath+'\ConfigFiles\config.json')
    api_key = config["api_key"]
    city = config["city"]
    botToken= config["bot_token"]
    if not api_key or not city:   ## esto quedo colgado, no esta mal... pero...
        print("Asegúrate de configurar las variables de entorno OPENWEATHERMAP_API_KEY y OPENWEATHERMAP_CITY.")
        return
    ###
    
    # Programa las llamadas a las funciones en intervalos diferentes
    #schedule.every(1).hour.do(pronosticos.obtener_pronostico_actual, api_key=api_key, city=city)
    #schedule.every(3).hours.do(pronosticos.obtener_pronostico_corto_plazo, api_key=api_key, city=city)
    schedule.every().day.at("09:05").do(pronosticos.obtener_pronostico_futuro, api_key=api_key, city=city)
    outputPronostico=pronosticos.obtener_pronostico_futuro(api_key=api_key,city=city)

    bot_send_msg(botToken,5178063489,outputPronostico)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()
