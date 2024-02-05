# weatherAlert
Project to set a simple workflow that checks the weather for the next days and alerts if it will be a rainy day or not

to update policy if the virtual env doesnt work
Set-ExecutionPolicy Unrestricted -Scope Process

##API CALLS
current weather data -- https://openweathermap.org/current
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

5days forecast -- https://openweathermap.org/forecast5
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}