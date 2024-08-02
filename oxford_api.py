import requests
import json


"""Enter keys to authentication process and choose language"""
app_id = '248b9f02'
app_key = '12124925ade46a8d7e65a48e1f10b753'
language = 'en-us'

"""get world to search on oxford"""
word_id = str(input("Enter a World you want to see in oxford:"))


url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word_id}"

headers = {'app_id': app_id,'app_key': app_key}

response = requests.get(url, headers=headers,timeout=10)

"""to check  output and print data in jason format"""
print(response.status_code)
print(response.json())

