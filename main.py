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
        self._observations.append(obs)

    def __repr__(self):
       return str((self.get_id(), self.get_origin(), self.get_storm_num(), self.get_year(), self.get_name(), len(self.get_observations())))


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

file = open("./storms_three_years.csv")

data = csv.DictReader(file)
origin_year_dict = dict()

# data for OUTPUT 1
for line in data:
    origin = line["ID"][:2]
    year = line["Date"][:4]
    name = line["Name"].strip()
    storm = Storm(line["ID"], origin, line["ID"][2:4], year, name)
    observation = Observation(storm, line["Date"], line["Time"], line["Status"], line["Latitude"], line["Longitude"], line["Maximum Wind"], line["Minimum Pressure"])
    if not origin_year_dict.get((origin, year)):
        # create first entry
        storm.add_observation(observation)
        origin_year_dict[(origin, year)] = [storm]
    else:
        # add storm to entry list
        found_storm = False
        for s in origin_year_dict[(origin, year)]:
            if s.get_name() == storm.get_name():
                found_storm = True
                s.add_observation(observation)
        if not found_storm:
            storm.add_observation(observation)
            origin_year_dict[(origin, year)].append(storm)
    
# display OUTPUT 1
print("OUTPUT 1")
keys = []
for k in origin_year_dict.keys():
    keys.append(k)
keys.sort(reverse=True, key=lambda k: k[0])
keys.sort(reverse=True, key=lambda k: k[1])

for key in keys:
    year = key[1]
    origin = key[0]
    names = []
    for s in origin_year_dict[key]:
        names.append(s.get_name())
    names.sort(reverse=False)
    print(str(year) + " " + str(origin) + " " + str(len(names)) + " " + str(names))

# data for OUTPUT 2
print("\nOUTPUT 2")
years_dict = {}
name_max_min = []
year_obs_dict = {}

for origin, year in origin_year_dict.keys():
    if not  year_obs_dict.get(year):
        year_obs_dict[year] = origin_year_dict[(origin, year)]
    else:
        year_obs_dict[year] += origin_year_dict[(origin, year)]

obs_list = []
max_list = []
for key in sorted(year_obs_dict.keys(), reverse=True):
    print(str(key) + " " + str(len(year_obs_dict[key])))
    for storm in year_obs_dict[key]:
        ob = storm.get_observations()
        obs_list = []
        for o in ob:
            obs_list.append([o.get_storm().get_name(), int(o.get_max_wind()), int(o.get_min_pressure())])
        obs_list.sort(reverse=True, key=lambda x: x[1])
        max_list.append(obs_list[0])
    max_list.sort(reverse=True, key=lambda x: x[1])
    for m in max_list:
        print(str(m[0])+" "+str(m[1]) + " " + str(m[2]))
    max_list = []
    print()