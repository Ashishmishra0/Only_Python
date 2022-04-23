import requests

My_Lat = 22.719568
My_Lang = 75.857727

parameters = {
    "lat": My_Lat,
    "lng": My_Lat,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))
print(sunset.split("T" ))
