import schedule
import time
import pronosticos
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
import logging
logger = logging.getLogger(__name__)

#from Drivers.drvConfig import readConfigFile

import Drivers.drvLogger as drvLogger

def main():
    ## INIT CONFIG
    drvLogger.initLogger()
    ### read config File
    api_key = os.environ["API_KEY"]
    city = os.environ["CITY"]
    botToken= os.environ['BOT_TOKEN']
    destinatary=os.environ['BOT_DESTINATARY']
    
    logger.info("MAIN - environment variables loaded")
    
    # Programa las llamadas a las funciones en intervalos diferentes
    #schedule.every(1).hour.do(pronosticos.obtener_pronostico_actual, api_key=api_key, city=city)
    #schedule.every(3).hours.do(pronosticos.obtener_pronostico_corto_plazo, api_key=api_key, city=city)
    schedule.every().day.at("07:00").do(pronosticos.obtener_pronostico_futuro, api_key=api_key, city=city,botToken=botToken,destinatary=destinatary)
    schedule.every().day.at("10:21").do(pronosticos.obtener_pronostico_actual, api_key=api_key, city=city,botToken=botToken,destinatary=destinatary)
    schedule.every().day.at("16:00").do(pronosticos.obtener_pronostico_actual, api_key=api_key, city=city,botToken=botToken,destinatary=destinatary)
    
    #outputPronostico=pronosticos.obtener_pronostico_futuro(api_key=api_key,city=city,botToken=botToken,destinatary=destinatary)
    while True:
        schedule.run_pending()
        time.sleep(300)

if __name__ == "__main__":
    main()
