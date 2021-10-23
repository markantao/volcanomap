import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[43.65405369289918, -79.38369434349275], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

#zip function is used to iterate between two lists with one for loop. Distributes the items one by one.
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")