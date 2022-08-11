import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


"""
    [x] --> Content Source = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"
"""

filename = "data/content_past_30_days.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, hover_texts = [], []
lons, lats =[], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    # Adding Hover Text
    title = eq_dict['properties']['title']
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
                # ----OR----
data = [
    {
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # Customizing Marker Size
    'marker': {
        'size': 5,
        'color': mags,
        'colorscale': 'Viridis',    #--> more color option can be found using {show_color_scale.py} file.
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'},
    },
}
    ]
my_layout = Layout(title="Global Earthquakes.")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="global_earthquakes.html")


