import requests
from datetime import datetime
my_lat = 20.593683
my_lng = 78.962883
parameters = {
    "lat": my_lat,
    "lng":my_lng,
    "formatted":0
}
time_now = datetime.now()
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(time_now.hour)


