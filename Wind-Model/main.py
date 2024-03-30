# ADD STUFF HERE!
import API_KEY
import requests
import json

params = "waterTemperature,wavePeriod,waveDirection,waveHeight,windWaveDirection,windWaveHeight,windWavePeriod,swellPeriod,secondarySwellPeriod,swellDirection,secondarySwellDirection,swellHeight,secondarySwellHeight,windSpeed,windSpeed20m,windSpeed30m,windSpeed40m,windSpeed50m,windSpeed80m,windSpeed100m,windSpeed1000hpa,windSpeed800hpa,windSpeed500hpa,windSpeed200hpa,windDirection,windDirection20m,windDirection30m,windDirection40m,windDirection50m,windDirection80m,windDirection100m,windDirection1000hpa,windDirection800hpa,windDirection500hpa,windDirection200hpa,airTemperature,airTemperature80m,airTemperature100m,airTemperature1000hpa,airTemperature800hpa,airTemperature500hpa,airTemperature200hpa,precipitation,gust,cloudCover,humidity,pressure,visibility,currentSpeed,currentDirection,iceCover,snowDepth,seaLevel"
response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 40.112283,
    'lng': -88.226541,
    'params': params,
  },
  headers={
    'Authorization': API_KEY.API_KEY
  }
)

json_data = response.json()
print(json_data)


with open("./out.json", "a") as f:
    f.write(str(json_data))





