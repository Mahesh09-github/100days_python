import requests
from twilio.rest import Client 

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "b39476cc49d2d0936d64adbfe71f6cf4"
LAT=-13.962612
LON=33.774120
account_id = "ACf5b643cad2afab67de1286e558c5dcb8"
auth_token = "7c3e7c2d96b687f7e2841f26771eef6a"
weather_params = {
    "lat":LAT,
    "lon":LON,
    "appid":api_key,
    "cnt":4
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    print(hour_data)
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_id,auth_token)
    message = client.messages.create(
    body="Today,It is going to rain,don't forget to carry umbrella",
    from_="+13502474949",
    to="+916301664716"
    )
else:
    client = Client(account_id,auth_token)
    message = client.messages.create(
    body="Not Going to Rain",
    from_="+13502474949",
    to="+916301664716"
    )                      
