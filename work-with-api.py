import requests

lat = 48.5
long = 2.35

# API URL

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m"

response = requests.get(url)
data = response.json()
data["current"]

type(data)
isinstance(data, dict)

js_weath = data.items()

temp = data["current"]["temperature_2m"]
for key,val in js_weath:
    print("Weather Details as follow ")
    print(f"\n Detail: {key} - Val: {val}")

def get_weather(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"],data["elevation"]

pairs_weather = get_weather(47.9,3.75)
lon_weather = get_weather(51.50,-0.12)
tok_weather = get_weather(35.68,139.69)

print(f"Paris Temp {pairs_weather[0]} Elevation: {pairs_weather[1]}")
print(f"Lon Temp {lon_weather[0]}  Elevation: {lon_weather[1]}")
print(f"Tok Temp {tok_weather[0]} Elevation: {tok_weather[1]}")