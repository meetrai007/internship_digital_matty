import requests
import json
import logging
logging.basicConfig(level=logging.INFO)



def find_temp():
    logging.debug("find_temp function start")
    location=str(input("Enter your location to find weather:"))
    user_key=("720eb36df944497d90661207242807")
    url=(f"http://api.weatherapi.com/v1/current.json?key={user_key}&q={location}&aqi=yes")
    response=requests.get(url,timeout=10)

    weather_data=response.json()

    loc=weather_data["location"]["name"]
    temp=weather_data["current"]["temp_c"]

    logging.info(f"temp in {loc} is {temp} celsius")
    logging.debug("find_temp function end")

find_temp()