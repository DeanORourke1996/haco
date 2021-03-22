import json
import requests

api_key = "ovSgAFhrQK3uDVyGdWyab6zDT6EnzzVe5kizXf8k"
url = "https://api.ambeedata.com/latest/fire"
querystring = {"lat": "12.9889055", "lng": "77.574044"}
headers = {
    'x-api-key': api_key,
    'Content-type': "application/json"
}

response = requests.request("GET", url, headers=headers, params=querystring)

if response:
    print("Connection Successful")
    print(response.text)
else:
    print("Connection Unsuccessful")

