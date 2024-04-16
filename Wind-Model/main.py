# ADD STUFF HERE!
import util.key_rotator as keys
import util.stormglass
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import util.nogo as nogo
import util.locations as locations
import util.parse_windycom

# CONFIGURATION
# latlong = (35.346656, -117.809655)
# latlong = (38.970604, -80.220575)
# latitude = latlong[0]
# longitude = latlong[1]

location = locations.LaunchSite.FAR

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



# low_altitude_wind_ok = nogo.Condition(0, 11.5)



# go_nogo = nogo.LaunchConditions()
# go_nogo.add_cond(low_altitude_wind_ok)
#################

dataloader = util.stormglass.StormGlass(key_rotator)
# dataloader.generate(location)
# dataloader.dump_file("./out_far_2.json")


dataloader.load_file("./out_far_2.json")


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
    a1, s1, _ = row.get_wind_gradient_raw()
    a2, s2, _ = grad_wdcom = util.parse_windycom.get_gradient_raw()

    a = a1
    s = s1

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

    # launch states
    good = max_wind < 20 and max_ha_wind < 35 and cc < 50 and pcp < 0.5 and gusts < 20
    mid = max_wind < 30 and max_ha_wind < 45 and cc < 65 and pcp < 1 and gusts < 30

    lc_ok.append(good)
    lc_mid.append(mid)



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
plt.legend(loc='upper right')

# plt.vlines((6*24)+23 ,0,100,linestyles='dashed',colors='black')
# plt.vlines((7*24)+0 ,0,100,linestyles='solid',colors='red')

# plt.fill_between(range(hours), 0, 100, where=lc_bad, facecolor='red', alpha=.1)
plt.fill_between(range(hours), 0, 100, where=lc_mid, facecolor='yellow', alpha=.3)
plt.fill_between(range(hours), 0, 100, where=lc_ok, facecolor='green', alpha=.3)


# ax.set_xlabel("Altitude (m)")
# ax.set_ylabel("Wind speed (m/s)")
# ax.set_zlabel("Hour")

plt.show()

      
    




