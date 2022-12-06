import folium

map = folium.Map(location = [46.7712, 23.6236], zoom_start=6, tiles="Stamen Terrain")

for cdn in [[46.7712, 23.6236], [47.5525, 25.8856], [44.1598, 28.6348], [47.5289, 21.6254], [48.1351, 11.5820], [41.3874, 2.1686], [36.75, -3.88], [54.6872, 25.2797], [59.3293, 18.0686], [59.9139, 10.7522]]:
  map.add_child(folium.Marker(location=cdn, popup="New Marker", icon=folium.Icon(color="green")))

map.save("Map1.html")