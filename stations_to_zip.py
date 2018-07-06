import json
from geopy.geocoders import Nominatim
geolocator = Nominatim()

def write_to_file(station_id, station_zip):
  with open('station_zips.txt', 'a') as file:
    file.write(station_id + ' ' + station_zip)
    file.write('\n')

def coord_to_zip(lat, long):
  location = geolocator.reverse(lat + ',' + long)
  return location.raw['address']['postcode']

with open('stations.json') as file:
  stations = json.load(file)

for station in stations.items():
  print('processing station id: ' + station[0])
  current_station_id = station[0]
  current_station_lat = station[1]['latitude']
  current_station_long = station[1]['longitude']

  current_station_zip = coord_to_zip(current_station_lat, current_station_long)
  write_to_file(current_station_id, current_station_zip)