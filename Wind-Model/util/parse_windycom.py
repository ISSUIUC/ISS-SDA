import json
##############################################################

# Edit data below for parsing windy.com data.
windy_data_in = open("./Wind-Model/extern/output_1713205174590_FAR.json", "r", encoding="utf-8")

##############################################################

windy_data = json.loads(windy_data_in.read())

# Time to get windy
def get_windy_raw():
    return windy_data

def get_gradient_raw():
    json_raw = get_windy_raw()

    CONST_ALTS = [0, 100, 600, 750, 900, 1500, 2000, 3000, 4200, 5500, 7000, 9000, 10000, 11700, 13500, 30000]

    out = {}
    data = json_raw[0]
    alts = []
    for i in range(len(CONST_ALTS)):
        alts.append(CONST_ALTS[i])
    return alts, data['speeds'], data['directions']

def get_data(i):
    json_raw = get_windy_raw()

    CONST_ALTS = [0, 100, 600, 750, 900, 1500, 2000, 3000, 4200, 5500, 7000, 9000, 10000, 11700, 13500, 30000]

    out = {}
    data = json_raw[i]
    alts = []
    for i in range(len(CONST_ALTS)):
        alts.append(CONST_ALTS[i])
    return alts, data['speeds'], data['directions']
