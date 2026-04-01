import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
api_id = os.getenv("API_ID")
api_key = os.getenv("API_KEY")
authorization_ = os.getenv("AUTHORIZATION_")

endpoint = os.getenv("ENDPOINT")
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

today = datetime.now()

parameters = {
    "query": input("What Exercise did you do today? ")
}
api_headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

response = requests.post(url=endpoint,headers=api_headers,json=parameters)
data = response.json()["exercises"]
print(data)

sheety_data = {
    "workout":{
        "date":today.strftime("%d/%m/%Y"),
        "time":today.strftime("%H:%M:%S"),
        "exercise":data[0]["name"],
        "duration":data[0]["duration_min"],
        "calories":data[0]["nf_calories"]
    }
}
authorization = {
    "Authorization": authorization_
}

sheety_response  = requests.post(url=sheety_endpoint,json=sheety_data,headers=authorization)
sheety_response.raise_for_status()
sheety_data = response.json()
print(sheety_data)
