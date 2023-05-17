class Town:
    def __init__(self, name):
        self.name = name
        self.lattidude = ""
        self.longitude = ""

    def set_latitude(self, a):
        self.latitude = a

    def set_longitude(self, b):
        self.longitude = b

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
