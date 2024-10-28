

def interleave_gradient(gradient_1, gradient_2):
    out = {}

    for key, value in gradient_1:
        if out[key] is None:
            out[key] = value
        else:
            if out[key]['speed'] < value['speed']:
                out[key] = value
    
    for key, value in gradient_2:
        if out[key] is None:
            out[key] = value
        else:
            if out[key]['speed'] < value['speed']:
                out[key] = value



def to_gradient(altitudes, wind_speeds, wind_directions):
    return_dict = {}

    # Finally construct return dictionary
    for i in range(len(altitudes)):
        return_dict[altitudes[i]] = {"speed": wind_speeds[i], "direction": wind_directions[i]}
    return return_dict