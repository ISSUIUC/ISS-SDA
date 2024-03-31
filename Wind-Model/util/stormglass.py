# Wrapper for the stormglass API
# ISS-SDA 2024
import requests
import datetime
import json
import math

def altitude_from_pressure_temperature(pressure_mb, temperature_C):
    altitude = (-math.log(pressure_mb * 0.000987) * (temperature_C + 273.15) * 29.254);
    return altitude

class StormGlassDataRow:
    # A wrapper for the dictionary returned by StormGlassData __getitem__ operator
    # Allows us to use it as a normal dictionary, but to also add special methods to it for data parsing purposes
    def __init__(self, inner_dict) -> None:
        self.data__ = inner_dict
    
    def __getitem__(self, key):
        return self.data__[key]
    
    def __setitem__(self, key, value):
        self.data__[key] = value

    def __delitem__(self, key):
        del self.data__[key]
    
    def __str__(self):
        return str(self.data__)

    # Dict methods
    def keys(self):
        return self.data__.keys()

    def items(self):
        return self.data__.items()
    
    def values(self):
        return self.data__.items()
    
    # Actual calculations
    def get_wind_gradient_raw(self):
        direct_alt_match_keys = ["", "20m", "30m", "40m", "50m", "80m", "100m"]
        pres_match_keys = ["800hpa", "500hpa", "200hpa"]
        pres_match_values = [800, 500, 200]
        altitudes = [10, 20, 30, 40, 50, 80, 100]

        wind_directions = [self.data__['windDirection' + i] for i in direct_alt_match_keys]
        wind_speeds =  [self.data__['windSpeed' + i] for i in direct_alt_match_keys]
        temps =  [self.data__['airTemperature' + i] for i in pres_match_keys]

        computed_altitudes = []
        for i in range(len(pres_match_values)):
            pres = pres_match_values[i]
            temp = temps[i]

            wind_directions.append(self.data__['windDirection' + pres_match_keys[i]])
            wind_speeds.append(self.data__['windSpeed' + pres_match_keys[i]])

            computed_altitudes.append(altitude_from_pressure_temperature(pres, temp))

        altitudes = altitudes + computed_altitudes
        return altitudes, wind_speeds, wind_directions

    def get_wind_gradient(self):
        # Returns an array of dictionaries where the key is the altitude and value is wind speed/direction at that altitude.
        altitudes, wind_speeds, wind_directions = self.get_wind_gradient_raw()
        return_dict = {}

        # Finally construct return dictionary
        for i in range(len(altitudes)):
            return_dict[altitudes[i]] = {"speed": wind_speeds[i], "direction": wind_directions[i]}
        return return_dict
    
    def plot_wind_speed_gradient(self, context):
        a, s, _ = self.get_wind_gradient_raw()
        context.plot(a, s)

class StormGlassData:
    def __init__(self, sg_json, weather_model) -> None:
        self.data__ = sg_json
        self.wm__ = weather_model

    def get_model_data__(self, dct):
        if(type(dct) == str):
            return dct
        return dct.get(self.wm__)


    def __getitem__(self, key):
        if(key == -1):
            return self.data__['meta']
        
        if isinstance(key, slice):
            # Slice operator
            indices = range(*key.indices(len(self.data__['hours'])))
            return [StormGlassDataRow({k: self.get_model_data__(v) for k,v in self.data__['hours'][k_].items()}) for k_ in indices]
        return StormGlassDataRow({k: self.get_model_data__(v) for k,v in self.data__['hours'][key].items()})
    
    def __setitem__(self, key, value):
        print("WARN: __setitem__ called explicitly on StormGlassData object")
        self.data__[key] = value
    
    def __delitem__(self, key):
        del self.data__[key]
    

class StormGlass:
    # Static list of all allowed parameters for the API
    # This wrapper retrieves all available data on the API and filters it later.
    weather_request_params__ = "waterTemperature,wavePeriod,waveDirection,waveHeight,windWaveDirection,windWaveHeight,windWavePeriod,swellPeriod,secondarySwellPeriod,swellDirection,secondarySwellDirection,swellHeight,secondarySwellHeight,windSpeed,windSpeed20m,windSpeed30m,windSpeed40m,windSpeed50m,windSpeed80m,windSpeed100m,windSpeed1000hpa,windSpeed800hpa,windSpeed500hpa,windSpeed200hpa,windDirection,windDirection20m,windDirection30m,windDirection40m,windDirection50m,windDirection80m,windDirection100m,windDirection1000hpa,windDirection800hpa,windDirection500hpa,windDirection200hpa,airTemperature,airTemperature80m,airTemperature100m,airTemperature1000hpa,airTemperature800hpa,airTemperature500hpa,airTemperature200hpa,precipitation,gust,cloudCover,humidity,pressure,visibility,currentSpeed,currentDirection,iceCover,snowDepth,seaLevel"

    def __init__(self, API_key) -> None:
        self.API_key: str = API_key
        self.sg_data__ = None
        self.weather_model__ = "noaa"

    def generate(self, lat:float, long:float, start: datetime.datetime = datetime.datetime.now(), end: datetime.datetime = datetime.datetime.max):
        request_params = {'lat': lat, 'lng': long, 'params': self.weather_request_params__}

        if (start is not None):
            request_params['start'] = int(start.timestamp())
        
        if (end != datetime.datetime.max):
            request_params['end'] = int(end.timestamp())

        response = requests.get('https://api.stormglass.io/v2/weather/point', params=request_params, headers={'Authorization': self.API_key})
        self.data = response.json()

    def set_weather_model(self, new_model):
        self.weather_model__ = new_model

    def load_file(self, filepath):
        with open(filepath, "r") as f:
            self.sg_data__ = json.loads(f.read())

    def dump_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(json.dumps(self.data))

    def get_dataframe(self):
        return StormGlassData(self.sg_data__, self.weather_model__)



    