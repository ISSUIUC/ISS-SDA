# ADD STUFF HERE!
import API_KEY
import util.stormglass
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import util.nogo as nogo

# CONFIGURATION
latitude = 40.112283
longitude = -88.226541


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



# low_altitude_wind_ok = nogo.Condition(0, 11.5)



# go_nogo = nogo.LaunchConditions()
# go_nogo.add_cond(low_altitude_wind_ok)
#################

dataloader = util.stormglass.StormGlass(API_KEY.API_KEY)
dataloader.load_file("./dl_out_2.json")
# dataloader.generate(latitude, longitude)
# dataloader.dump_file("./dl_out_2.json")


df: util.stormglass.StormGlassData = dataloader.get_dataframe()

# ax = plt.figure().add_subplot(projection='3d')

max_winds = []
max_hl_winds = []
cc_l = []
pcp_l = []
gust_l = []

lc_ok = []
lc_mid = []

hours = len(df)

for ind, row in enumerate(df):
    a, s, _ = row.get_wind_gradient_raw()
    cc = row.cloud_cover()
    pcp = row.precipitation()
    gusts = row.gusts()

    max_wind = -1
    for i in range(8):
        if s[i] > max_wind:
            max_wind = s[i]

    max_ha_wind = -1
    for i in range(8, len(s)):
        if s[i] > max_ha_wind:
            max_ha_wind = s[i]

    max_winds.append(max_wind)
    max_hl_winds.append(max_ha_wind)

    cc_l.append(cc)
    pcp_l.append(pcp)
    gust_l.append(gusts)

    lc_ok.append(max_wind < 20 and max_ha_wind < 35 and cc < 50 and pcp < 1 and gusts < 20)
    lc_mid.append(max_wind < 30 and max_ha_wind < 65 and cc < 70 and pcp < 2 and gusts < 30)


    # Launch condition check


ts = [prettytime(utc_datetime(df[h]['time']).astimezone(tz)) for h in range(hours)]
ts = [i for i in range(hours)]
plt.plot(ts, max_winds, label='Low altitude wind (m/s)')
plt.plot(ts, max_hl_winds, label = "High altitude wind (m/s)")
plt.plot(ts, cc_l, label="Cloud cover (%)")
plt.plot(ts, pcp_l, label="Precipitation (mm/hr)")
plt.plot(ts, gust_l, label="Ground level Gusts (m/s)")

plt.xlabel(f"Time (Hours since {prettytime_full(utc_datetime(df[0]['time']).astimezone(tz))})")
plt.ylabel("Parameter value (varied)")
plt.legend(loc='upper left')

plt.fill_between(range(hours), 0, 100, where=lc_mid, facecolor='yellow', alpha=.5)
plt.fill_between(range(hours), 0, 100, where=lc_ok, facecolor='green', alpha=.5)


# ax.set_xlabel("Altitude (m)")
# ax.set_ylabel("Wind speed (m/s)")
# ax.set_zlabel("Hour")

plt.show()

      
    




