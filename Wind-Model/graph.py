import matplotlib.pyplot as plt
import math
import numpy as np

datapoint = {"airTemperature": {"noaa": 16.03, "sg": 16.03}, "airTemperature1000hpa": {"noaa": 17.21, "sg": 17.21}, "airTemperature100m": {"noaa": 17.2, "sg": 17.2}, "airTemperature200hpa": {"noaa": -63.69, "sg": -63.69}, "airTemperature500hpa": {"noaa": -20.03, "sg": -20.03}, "airTemperature800hpa": {"noaa": 4.35, "sg": 4.35}, "airTemperature80m": {"noaa": 17.23, "sg": 17.23}, "cloudCover": {"noaa": 100.0, "sg": 100.0}, "gust": {"noaa": 8.33, "sg": 8.33}, "humidity": {"noaa": 52.1, "sg": 52.1}, "iceCover": {"noaa": 0.0, "sg": 0.0}, "precipitation": {"noaa": 0.13, "sg": 0.13}, "pressure": {"noaa": 1013.05, "sg": 1013.05}, "snowDepth": {"noaa": 0.0, "sg": 0.0}, "time": "2024-03-30T00:00:00+00:00", "visibility": {"noaa": 24.13, "sg": 24.13}, "waterTemperature": {"noaa": 14.25, "sg": 14.25}, "windDirection": {"noaa": 179.69, "sg": 179.69}, "windDirection1000hpa": {"noaa": 268.26, "sg": 268.26}, "windDirection100m": {"noaa": 185.45, "sg": 185.45}, "windDirection200hpa": {"noaa": 270.01, "sg": 270.01}, "windDirection20m": {"noaa": 268.24, "sg": 268.24}, "windDirection30m": {"noaa": 268.1, "sg": 268.1}, "windDirection40m": {"noaa": 268.58, "sg": 268.58}, "windDirection500hpa": {"noaa": 270.01, "sg": 270.01}, "windDirection50m": {"noaa": 268.83, "sg": 268.83}, "windDirection800hpa": {"noaa": 269.93, "sg": 269.93}, "windDirection80m": {"noaa": 269.26, "sg": 269.26}, "windSpeed": {"noaa": 3.41, "sg": 3.41}, "windSpeed1000hpa": {"noaa": 0.11, "sg": 0.11}, "windSpeed100m": {"noaa": 7.29, "sg": 7.29}, "windSpeed200hpa": {"noaa": 55.23, "sg": 55.23}, "windSpeed20m": {"noaa": 0.13, "sg": 0.13}, "windSpeed30m": {"noaa": 0.14, "sg": 0.14}, "windSpeed40m": {"noaa": 0.21, "sg": 0.21}, "windSpeed500hpa": {"noaa": 25.58, "sg": 25.58}, "windSpeed50m": {"noaa": 0.28, "sg": 0.28}, "windSpeed800hpa": {"noaa": 7.27, "sg": 7.27}, "windSpeed80m": {"noaa": 0.52, "sg": 0.52}}
use_model = "noaa"

def altitude_from_pressure_temperature(pressure_mb, temperature_C):
    altitude = (-math.log(pressure_mb * 0.000987) * (temperature_C + 273.15) * 29.254);
    
    return altitude

def get_model_data(dct):
    if(type(dct) == str):
        return dct
    return dct.get(use_model)

def parse_data(dp):
    noaa_data = {}
    for k, v in dp.items():
        noaa_data[k] = get_model_data(v)
    

    # print(noaa_data)

    alt_data_keys = ["windDirection", "windSpeed"]
    direct_alt_match_keys = ["", "20m", "30m", "40m", "50m", "80m", "100m"]
    pres_match_keys = ["1000hpa", "800hpa", "500hpa", "200hpa"]
    pres_match_values = [1000, 800, 500, 200]
    direct_alt_match_values = [10, 20, 30, 40, 50, 80, 100]

    alts = direct_alt_match_values

    wind_directions = [noaa_data[alt_data_keys[0] + i] for i in direct_alt_match_keys]
    wind_speeds =  [noaa_data[alt_data_keys[1] + i] for i in direct_alt_match_keys]

    # print(alts)
    # print(wind_directions)
    # print(wind_speeds)


    # calc alt from pressure + temp
    temps =  [noaa_data['airTemperature' + i] for i in pres_match_keys]


    computed_altitudes = []
    for i in range(len(pres_match_values)):
        pres = pres_match_values[i]
        temp = temps[i]

        computed_altitudes.append(altitude_from_pressure_temperature(pres, temp))


    print(computed_altitudes)




parse_data(datapoint)