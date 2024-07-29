import requests
import json

"""get name to guess age"""
name=str(input("Enter your name :"))

"""free api to guesss age by name"""
url=f"https://api.agify.io/?name={name}"

"""get response and print"""
response=requests.get(url,timeout=10)
data=response.json()

print(f"name:{data["name"]}\nage:{data["age"]}")
