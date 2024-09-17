import scipy.stats as stats
import numpy as np

# interweaves stormglass data with windy.com data, and uses linear regression to allow data collection at every 100 ft

def interweave(sg_alt, windy_alt, sg_speed, windy_speed):
    assert len(sg_alt) == len(sg_speed) and len(windy_alt) == len(windy_speed), "Lengths of input arrays do not match"

    # convert speed1 from m/s to mph
    sg_speed = [x * 2.23694 for x in sg_speed]

    # convert speed2 from knots to mph
    windy_speed = [x * 1.15078 for x in windy_speed]

    # convert altitudes to feet
    sg_alt = [x * 3.28084 for x in sg_alt]
    windy_alt = [x * 3.28084 for x in windy_alt]

    # sg_alt = [10, 20, 30, 40, 50, 80, 100, 2021.4304428818893, 5435.471817385999, 10148.554144119416] in meters
    # windy_alt = [0, 100, 600, 750, 900, 1500, 2000, 3000, 4200, 5500, 7000, 9000, 10000, 11700, 13500, 30000] in m
    
    # create linspace across entire range
    sg_x = np.linspace(0, 32000, num = 321)
    windy_x = np.linspace(0, 98000, num = 981)

    sg_y = []
    windy_y = []

    # iterate through each altitude from the linspaces (1000 ft increments)
    # and find the speed at that altitude using linear regression, matching it bewteen two altitute points from the sources

    for alt in sg_x:
        # find the altitude right below the current altitude
        below_alt = max([x for x in sg_alt if x <= alt], default=0)
        # find the altitude right above the current altitude
        above_alt = min([x for x in sg_alt if x >= alt])
        # find the index of the below_alt and above_alt in sg_alt
        if below_alt == 0:
            below_index = 0
        else:
            below_index = sg_alt.index(below_alt)
        above_index = sg_alt.index(above_alt)
        if (below_index == above_index):
            sg_y.append(sg_speed[below_index])
            continue
        # perform linear regression between the below and above altitudes
        slope, intercept, _, _, _ = stats.linregress([below_alt, above_alt], [sg_speed[below_index], sg_speed[above_index]])
        # calculate the speed at the current altitude using the linear regression equation
        sg_y.append(slope * alt + intercept)

        
        


    for alt in windy_x:
        # find the altitude right below the current altitude
        below_alt = max([x for x in windy_alt if x <= alt], default = 0)
        # find the altitude right above the current altitude
        above_alt = min([x for x in windy_alt if x >= alt])
        # find the index of the below_alt and above_alt in sg_alt
        if below_alt == 0:
            below_index = 0
        else:
            below_index = windy_alt.index(below_alt)
        above_index = windy_alt.index(above_alt)
        if (below_index == above_index):
            windy_y.append(windy_speed[below_index])
            continue
        # perform linear regression between the below and above altitudes
        slope, intercept, _, _, _ = stats.linregress([below_alt, above_alt], [windy_speed[below_index], windy_speed[above_index]])
        # calculate the speed at the current altitude using the linear regression equation
        windy_y.append(slope * alt + intercept)


    # fix this later (issue with mistmatched lengths for plotting)
    sg_y.append(sg_y[-1])


    # now compare speeds at each altitude, and take the max
    final_alts = windy_x
    final_speeds = []
    for i in range(len(final_alts)):
        if i > len(sg_y) - 1:
            final_speeds.append(windy_y[i])
        else:
            final_speeds.append(max(sg_y[i], windy_y[i]))
            # final_speeds.append((sg_y[i] + windy_y[i]) / 2)


    return final_alts, final_speeds





def interweave2(sg_alt, windy_alt, sg_speed, windy_speed):
    assert len(sg_alt) == len(sg_speed) and len(windy_alt) == len(windy_speed), "Lengths of input arrays do not match"

    # convert speed1 from m/s to mph
    sg_speed = [x * 2.23694 for x in sg_speed]

    # convert speed2 from knots to mph
    # windy_speed2 = [x * 1.15078 for x in windy_speed]

    # convert altitudes to feet
    sg_alt = [x * 3.28084 for x in sg_alt]
    # windy_alt2 = [x * 3.28084 for x in windy_alt]

    # sg_alt = [10, 20, 30, 40, 50, 80, 100, 2021.4304428818893, 5435.471817385999, 10148.554144119416] in meters
    # windy_alt = [0, 100, 600, 750, 900, 1500, 2000, 3000, 4200, 5500, 7000, 9000, 10000, 11700, 13500, 30000] in m
    
    # create linspace across entire range
    sg_x = np.linspace(0, 32000, num = 321)
    windy_x = np.linspace(0, 98000, num = 981)

    sg_y = []
    windy_y = []

    for i in sg_x:
        thing = np.interp(i, sg_alt, sg_speed)
        sg_y.append(thing)
    
    for i in windy_x:
        thing = np.interp(i, windy_alt, windy_speed)
        windy_y.append(thing)
    
    # fix this later (issue with mistmatched lengths for plotting)
    sg_y.append(sg_y[-1])

    # now compare speeds at each altitude, and take the max
    final_alts = windy_x
    final_speeds = []
    for i in range(len(final_alts)):
        if i > len(sg_y) - 1:
            final_speeds.append(windy_y[i])
        else:
            final_speeds.append(max(sg_y[i], windy_y[i]))
            # final_speeds.append((sg_y[i] + windy_y[i]) / 2)


    return final_alts, final_speeds








# old version of interweave that doesn't/barely works
def interweave_primitive(sg_alt, windy_alt, sg_speed, windy_speed, sg_dir, windy_dir):
    assert len(sg_alt) == len(sg_speed) == len(sg_dir) and len(windy_alt) == len(windy_speed) == len(windy_dir), "Lengths of input arrays do not match"

    # convert speed1 from m/s to mph
    sg_speed = [x * 2.23694 for x in sg_speed]

    # convert speed2 from knots to m/s
    windy_speed = [x * 0.514444 for x in windy_speed]

    alt_vs_speed = {}
    alt_vs_dir = {}

    for i in range(len(sg_alt)):
        alt_vs_speed[sg_alt[i]] = sg_speed[i]
    
    for i in range(len(windy_alt)):
        if (windy_alt[i] in alt_vs_speed):
            alt_vs_speed[windy_alt[i]] = max(alt_vs_speed[windy_alt[i]], windy_speed[i])
            # alt_vs_speed[windy_alt[i]] = (alt_vs_speed[windy_alt[i]] + windy_speed[i]) / 2
        else:
            alt_vs_speed[windy_alt[i]] = windy_speed[i]
    
    
    alt_vs_speed = dict(sorted(alt_vs_speed.items()))

    alts = list(alt_vs_speed.keys())
    speeds = list(alt_vs_speed.values())

    return alts, speeds

    