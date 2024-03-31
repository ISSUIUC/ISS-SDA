import matplotlib.pyplot as plt
import math
import numpy as np

import json

lat= 40.112283
lng= -88.226541

datapoint = None
with open("./out.json", "r") as of:
    all_data = of.read()

    data = json.loads(all_data)

    datapoint = data['hours'][10]


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
    pres_match_keys = ["800hpa", "500hpa", "200hpa"]
    pres_match_values = [800, 500, 200]
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

        wind_directions.append(noaa_data['windDirection' + pres_match_keys[i]])
        wind_speeds.append(noaa_data['windSpeed' + pres_match_keys[i]])

        computed_altitudes.append(altitude_from_pressure_temperature(pres, temp))


    alts = alts + computed_altitudes


    # for i in range(len(alts)):
    #     print("ALT:", alts[i], "m", "      ", "ws: ", wind_speeds[i], "m/s")

    plt.plot(alts, wind_speeds)
    plt.xlabel("Altitude (m)")
    plt.ylabel("Wind speed (m/s)")
    plt.title(f"Wind gradient at {datapoint['time']} @ ({lat},{lng})")
    plt.show()





parse_data(datapoint)