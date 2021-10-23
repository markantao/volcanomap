import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_maker(elevation):
    if elevation < 1000:
        return 'blue'
    if elevation >= 1000 and elevation < 2499:
        return 'green'
    if elevation > 2499:
        return 'red'

map = folium.Map(location=[43.65405369289918, -79.38369434349275], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

#zip function is used to iterate between two lists with one for loop. Distributes the items one by one.
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(el) + "m", fill_color=color_maker(el)
    , color="black", fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

map.save("Map1.html")