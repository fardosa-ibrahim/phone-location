
import folium
import geocoder


g=geocoder.ip("194.168.1.157")

myaddress=g.latlng

my_map=folium.Map(location=myaddress,zoom_start=12)
folium.CircleMarker(location=myaddress,radius=50,popup="karen").add_to(my_map)
folium.Marker(myaddress,popup="karen").add_to(my_map)

my_map.save("locate_me.html")