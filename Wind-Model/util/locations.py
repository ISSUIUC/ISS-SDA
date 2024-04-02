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
