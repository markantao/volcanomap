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

map = folium.Map(location=[43.62428891828346, -116.04618279665495], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

#zip function is used to iterate between two lists with one for loop. Distributes the items one by one.
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(el) + "m", fill_color=color_maker(el)
    , color="black", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl()) 
# Put this line below line above so that "FeatureGroup" and all added features will be part of the map whilst being able to toggle controls/features

map.save("Map1.html")