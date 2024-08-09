import requests
import json
import logging
logging.basicConfig(level=logging.INFO)

key="fca_live_iXvJQTDd64n7HUgVxQbzZGUpM3lkXA4gayQ5l7lU"
response=requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={key}",timeout=10)
data=response.json()
logging.debug(data)


current_type_list=[]
for index,keys in enumerate (data["data"],1):
    print(index,keys)
    current_type_list.append(keys)

input_index=int(input("choose your current currency:"))-1
current_currency=data["data"][current_type_list[input_index]]

input_index2=int(input("choose currency to convert:"))-1
new_currency=data["data"][current_type_list[input_index2]]

money=int(input("enter price to convert:"))
converted_currency=(money/current_currency)*new_currency
logging.info(f"your converted currency is {converted_currency} {current_type_list[input_index2]}")

