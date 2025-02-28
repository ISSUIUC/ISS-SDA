from enum import Enum

class Location:
    def __init__(self, lat, long) -> None:
        self.latitude = lat
        self.longitude = long

    def lat(self):
        return self.latitude
    
    def long(self):
        return self.longitude
    
    def latlong(self):
        return (self.latitude, self.longitude)

class LaunchSite(Enum):
    URBANA = Location(40.112283, -88.226541)
    ARGONIA = Location(37.166846, -97.739117)
    FAR = Location(35.347216, -117.808614)
    BONG = Location(42.635178, -88.127473)
    QCRC = Location(41.488008, -89.500092)
    PENCE = (40.3867, -87.5113)
