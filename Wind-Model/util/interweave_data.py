def interweave(alt1, alt2, speed1, speed2, dirs1, dirs2):
    assert len(alt1) == len(speed1) == len(dirs1) and len(alt2) == len(speed2) == len(dirs2), "Lengths of input arrays do not match"

    # # convert speed1 from m/s to mph
    # speed1 = [x * 2.23694 for x in speed1]

    # convert speed2 from knots to m/s
    speed2 = [x * 0.514444 for x in speed2]

    alt_vs_speed = {}
    alt_vs_dir = {}

    for i in range(len(alt1)):
        alt_vs_speed[alt1[i]] = speed1[i]
    
    for i in range(len(alt2)):
        if (alt2[i] in alt_vs_speed):
            # alt_vs_speed[alt2[i]] = max(alt_vs_speed[alt2[i]], speed2[i])
            alt_vs_speed[alt2[i]] = (alt_vs_speed[alt2[i]] + speed2[i]) / 2
        else:
            alt_vs_speed[alt2[i]] = speed2[i]
    
    
    alt_vs_speed = dict(sorted(alt_vs_speed.items()))

    alts = list(alt_vs_speed.keys())
    speeds = list(alt_vs_speed.values())

    # print(alts)
    # print()
    # print(speeds)
    # print()

    return alts, speeds

    