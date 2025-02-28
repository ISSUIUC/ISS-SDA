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
import util.locations as locations
import json
import numpy as np

#************************************#
# Look at the README for instructions on how to use!
file_name = "./inf_raw.json"
generate_new_data = False
location = locations.LaunchSite.FAR
#************************************#
OUTFILE_NAME = "out.json"
IS_SILENT = False
if(len(sys.argv) > 1):
    for i in range(len(sys.argv)):
        if(sys.argv[i] == "-s"):
            IS_SILENT = True
        if(sys.argv[i] == "-n"):
            generate_new_data = True
        if(sys.argv[i] == "--out"):
            OUTFILE_NAME = sys.argv[i+1]


# This accesses the API key and switches between the two. 
# We have a limited number of uses and the rotator takes turns using each key.
if(not IS_SILENT):
    print(f"Using outfile {OUTFILE_NAME}")
    print("Loading key rotator")
key_rotator = keys.APIKeyRotator("./Wind-Model/programdata/KEY_ROTATE_META.txt", "./Wind-Model/programdata/API_KEYS.txt")


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


if(not IS_SILENT):
    print("Loading stormglass data")
dataloader = util.stormglass.StormGlass(key_rotator)
if generate_new_data:
    dataloader.generate(location)
    dataloader.dump_file(file_name)

dataloader.load_file(file_name)
df: util.stormglass.StormGlassData = dataloader.get_dataframe()
if(not IS_SILENT):
    print("Data loaded")

out_data = []

if(not IS_SILENT):
    print("Converting data")

# Converts to a JSON file that our React App can read from
for i in range(len(df[0]['time'])):
    time = df[i]['time']
    sg_alts, sg_speeds, _ = df[i].get_wind_gradient_raw()
    sg_speeds = [x * 2.23694 for x in sg_speeds]
    sg_alts = [x * 3.28084 for x in sg_alts]

    MIN_PT = min(sg_alts)
    MAX_PT = max(sg_alts)

    alts = np.arange(0, MAX_PT, 100)
    speeds = np.interp(alts, sg_alts, sg_speeds)
    formatted_time = (prettytime_full(utc_datetime(time)))
    datarow = {"x": alts.tolist(), "y": speeds.tolist(), "title": "Wind Speed (mph) vs Altitude (ft) at " + formatted_time}
    out_data.append(datarow)

if(not IS_SILENT):
    print(f"Writing data to {OUTFILE_NAME}")
output_string = json.dumps(out_data)
with open(OUTFILE_NAME, "w") as outf:
    outf.write(output_string)

if(IS_SILENT):
    print(OUTFILE_NAME, end="")