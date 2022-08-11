import json


# Explore the structure of the data.
filename = "data/content_past_day_eq.json"
with open(filename) as f:
    all_eq_data = json.load(f)
    
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)


# Making a List of All Earthquakes
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags = []
lons, lats =[], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
# print(mags[:10])
# print(lons[:5])
# print(lats[:5])




