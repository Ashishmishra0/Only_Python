import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (latitude, longitude)
print(iss_position)
