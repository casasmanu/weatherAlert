import requests
from datetime import datetime , timedelta
import logging
logger = logging.getLogger(__name__)

from Drivers.drvTelegram import bot_send_msg

def obtener_pronostico_actual(api_key, city,botToken,destinatary):
    logger.info('obtener_pronostico_actual initiated')
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&units=metric&appid={api_key}"
    response = requests.get(current_url)
    logger.info('API called correctly')
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
    
    logger.info('Weather data parsed')
    textDateFromTimeStapm= str(datetime.fromtimestamp(pronTimeStamp))
    textSunsetTime=str(datetime.fromtimestamp(pronSunset))
    textSunriseTime=str(datetime.fromtimestamp(pronSunrise))

    output_text=f"{textDateFromTimeStapm} \n \
        Pronóstico Actual:{pronDesc} , {pronGral}\n \
        la temperatura es de {pronTempAct}°C y la sensacion termica {pronTempSens}°C \n \
        humedad %{pronTempHum} y presion {pronTempPres} Hpa \n \
        Viento: {pronWind} nudos? \n \
        hora de salida {textSunriseTime} puesta del sol {textSunsetTime}" 
    
    ####################################################################################
    logger.info('sending data')
    for retry in range(3):
        try:
            bot_send_msg(botToken,destinatary,output_text)
            break
        except Exception as e:
            logger.error(e)
    ####################################################################################
    
    logger.info(output_text)
    logger.info('pronostico_actual run correctly')
    return output_text



def obtener_pronostico_futuro(api_key, city,botToken,destinatary):
    logger.info('FUNC -- obtener_pronostico_futuro')
    current_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(current_url)
    logger.info('API called correctly')
    data = response.json()
    ### data to extract! --- take list values:
    ## parse Data
    dataArrayInDays=dataParserInDays(data)
    
    [dailyTempMax,dailyTempMin]=getLimitsForEachDay(dataArrayInDays)
    

    todayDate=datetime.today()
    tomorrowDate=todayDate+timedelta(days=1)
    overTomorrowDate=todayDate+timedelta(days=2)
    logger.info('Weather data parsed')

    output_text=f"maximas y minimas \n \
    {todayDate.day}.{todayDate.month} ----> {dailyTempMax[0]}°C | {dailyTempMin[0]}°C \n \
    {tomorrowDate.day}.{todayDate.month} ----> {dailyTempMax[1]}°C | {dailyTempMin[1]}°C \n \
    {overTomorrowDate.day}.{todayDate.month} ----> {dailyTempMax[2]}°C | {dailyTempMin[2]}°C" 
    
    ####################################################################################
    logger.info('sending data')
    for retry in range(3):
        try:
            bot_send_msg(botToken,destinatary,output_text)
            break
        except Exception as e:
            logger.error(e)
    ####################################################################################
    
    logger.info('obtener_pronostico_futuro run correctly')
    return output_text


def dataParserInDays(data):
## parse the values for the next 5 days, separating them in an array
   logger.info('dataParserInDays started')
   dateFormat='%Y-%m-%d %H:%M:%S'
   dataList=[[] for i in range(5)]
   todayDate=datetime.today()
   dataDateValue=datetime.strptime(data['list'][0]['dt_txt'],dateFormat).day
   j=0
   ## lets go for the next 5 days
   for i in range(0,5):
        ##todayDay=todayDate.day
        crrDate=todayDate+timedelta(days=i)
        crrDateDay=crrDate.day
        while(crrDateDay==dataDateValue and j<40):
            dataList[i].append(data['list'][j])
            dataDateValue=datetime.strptime(data['list'][j]['dt_txt'],dateFormat).day
            j+=1

   logger.info('dataParserInDays finished')
   return  dataList

def getLimitsForEachDay(lista:list):
    # double matrix to go each day, every 3 hours
    logger.info('getLimitsforEachDay started')
    maximosByDay=[]
    minimosByDay=[]
    #print("---------------------")
    for i in range (0,4) :
        klimit=len(lista[i])
        tempMaxList=[]
        tempMinList=[]
        #create the list for the temperatures
        #maybe is better to separate values before in data parser
        if (klimit==0):
            logger.info('getLimitsforEachDay - NULL VALUE IN PREDICIONTS CHECK pronosticos futuros')
            maximosByDay.append(0)
            minimosByDay.append(0)    
        else:    
            for j in range (0,klimit):
                tempMaxList.append(lista[i][j]['main']["temp_max"])
                tempMinList.append(lista[i][j]['main']["temp_min"])
                #print(tempMaxList[j])
            #print("\n")
            maximosByDay.append(max(tempMaxList))
            minimosByDay.append(min(tempMinList))
            #print(maximosByDay[i])
            #print("---------------------")
            
    logger.info('getLimitsforEachDay - finished running')
        

    return maximosByDay,minimosByDay