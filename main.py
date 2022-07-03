import phonenumbers
import opencage
from test import number
from phonenumbers import geocoder
import folium

pepnumber=phonenumbers.parse(number)
country=geocoder.description_for_number(pepnumber,'en')
print(country)

from phonenumbers import carrier
city_provider=phonenumbers.parse(number)
print(carrier.name_for_number(city_provider,'en'))

from opencage.geocoder import OpenCageGeocode
key="5beb66b25c694c10a61ac6d932831d2c"
geocoder=OpenCageGeocode(key)
query=str(country)
result=geocoder.geocode(query)
# print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=country).add_to(myMap)

myMap.save("mylocation.html")
