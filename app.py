import folium
map = folium.Map(location=[43.65405369289918, -79.38369434349275], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[43.2, -79.7], popup="Hi I am a marker!", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")