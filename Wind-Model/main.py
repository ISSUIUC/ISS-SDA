# ADD STUFF HERE!
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import util.key_rotator as keys
import util.stormglass
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import util.nogo as nogo
import util.locations as locations
# import util.parse_windycom
import util.interweave_data
import json

#************************************#
# Look at the README for instructions on how to use!
file_name = "./json_files/2-3-25.json"
generate_new_data = False
location = locations.LaunchSite.PENCE
#************************************#

# This accesses the API key and switches between the two. 
# We have a limited number of uses and the rotator takes turns using each key.

key_rotator = keys.APIKeyRotator("/Users/mihirshevade/ISS/Wind-Model/Wind-Model/programdata/KEY_ROTATE_META.txt", "/Users/mihirshevade/ISS/Wind-Model/Wind-Model/programdata/API_KEYS.txt")


def utc_datetime(utc_string):
    return datetime.strptime(utc_string, "%Y-%m-%dT%H:%M:%S%z")
    
tz = pytz.timezone('US/Central')


def prettytime(dt: datetime):
    s = ""
    hs = dt.hour
    if(dt.hour < 10):
        hs = "0" + str(hs)

    s = s + str(hs) + ":00"
    return s

def prettytime_full(dt: datetime):
    s = ""
    hs = dt.hour
    if(dt.hour < 10):
        hs = "0" + str(hs)


    s = s + str(dt.month) + "/" + str(dt.day) + " " + str(hs) + ":00"
    return s


dataloader = util.stormglass.StormGlass(key_rotator)
if generate_new_data:
    dataloader.generate(location)
    dataloader.dump_file(file_name)

dataloader.load_file(file_name)


df: util.stormglass.StormGlassData = dataloader.get_dataframe()


# Parses the data from the API
out_data = []
if generate_new_data:
    for ind, row in enumerate(df):
        time = df[ind]['time']
        sg_alts, sg_speeds, _ = row.get_wind_gradient_raw()
        # if using windy uncomment (currently not working)
        # windy_alts, windy_speeds, _ = util.parse_windycom.get_gradient_raw()
        # alts, speeds = util.interweave_data.interweave(sg_alts, windy_alts, sg_speeds, windy_speeds)
        alts = sg_alts
        speeds = sg_speeds
        formatted_time = (prettytime_full(utc_datetime(time).astimezone(tz)))
        datarow = {"x": alts, "y": speeds, "title": "Wind Speed (mph) vs Altitude (ft) at " + formatted_time}
        out_data.append(datarow)

# Converts to a JSON file that our React App can read from
for i in range(len(df[0]['time'])):
    time = df[i]['time']
    sg_alts, sg_speeds, _ = df[i].get_wind_gradient_raw()
    # Following two lines will be used if we want to use Windy.com (so above 30k ft)
    # windy_alts, windy_speeds = sunday3[i][0], sunday3[i][1]
    # alts, speeds = util.interweave_data.interweave2(sg_alts, windy_alts, sg_speeds, windy_speeds)
    sg_speeds = [x * 2.23694 for x in sg_speeds]
    sg_alts = [x * 3.28084 for x in sg_alts]
    alts = sg_alts
    speeds = sg_speeds
    formatted_time = (prettytime_full(utc_datetime(time)))
    datarow = {"x": alts, "y": speeds, "title": "Wind Speed (mph) vs Altitude (ft) at " + formatted_time}
    out_data.append(datarow)
    print(datarow)


output_string = json.dumps(out_data)


# with open("Wind-Model\my-app\src\main_data.json", "w+") as f:
#     f.write(output_string)

# DONE WITH JSON GENERATION