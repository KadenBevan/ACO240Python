import csv

class Storm():
    def __init__(self, i, o, s, y, n):
        self._id = i
        self._origin = o
        self._storm_num = s
        self._year = y
        self._name = n
        self._observations = []
    
    def get_id(self):
        return self._id

    def get_origin(self):
        return self._origin

    def get_storm_num(self):
        return self._storm_num

    def get_year(self):
        return self._year

    def get_name(self):
        return self._name

    def get_observations(self):
        return self._observations

    def add_observation(self, obs):
        pass

    def __repr__(self):
        return str((self.get_id(), self.get_origin(), self.get_storm_num, self.get_year, self.get_name, len(self.get_observations)))


class Observation():
    def __init__(self, s, d, t, st, lat, lon, mw, mp):
        self._storm = s
        self._date = d
        self._time = t
        self._status = st
        self._latitude = lat
        self._longitude = lon
        self._max_wind = mw
        self._min_pressure = mp

    def get_storm(self):
        return self._storm
    
    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_status(self):
        return self._status

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def get_max_wind(self):
        return self._max_wind

    def get_min_pressure(self):
        return self._min_pressure

    def __repr__(self):
        return str((self.get_storm().get_name(), self.get_date(), self.get_time(), self.get_latitude(), self.get_longitude(), self.get_max_wind(), self.get_min_pressure()))


data = csv.DictReader("storms_three_years.csv")
print(data)