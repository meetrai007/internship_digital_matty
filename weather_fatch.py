import requests
import json



def find_temp(location):
    location=str(input("Enter your location to find weather:"))
    user_key=("720eb36df944497d90661207242807")
    url=(f"http://api.weatherapi.com/v1/current.json?key={user_key}&q={location}&aqi=yes")
    response=requests.get(url,timeout=10)

    weather_data=response.json()

    loc=weather_data["location"]["name"]
    temp=weather_data["current"]["temp_c"]

    print(f"temp in {loc} is {temp} celsius")
