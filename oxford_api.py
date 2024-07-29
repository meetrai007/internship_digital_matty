import requests
import json

app_id = '248b9f02'
app_key = '12124925ade46a8d7e65a48e1f10b753'
language = 'en-us'
word_id = str(input("Enter a word you want to see in Oxford: "))

url = f"https://od-api.oxforddictionaries.com/api/v2/entries/{language}/{word_id}"

headers = {'app_id': app_id, 'app_key': app_key}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
