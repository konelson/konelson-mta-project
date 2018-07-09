import json

def write_to_file(station_id, station_name, lat, lng):
  with open('station_coords.csv', 'a') as file:
    file.write(station_id + ',' + station_name + ',' + lat + ',' + lng)
    file.write('\n')

with open('stations.json') as file:
  stations = json.load(file)

for station in stations.items():
  station_id = station[0]
  station_name = station[1]['station']
  station_lat = station[1]['latitude']
  station_lng = station[1]['longitude']
  write_to_file(station_id, station_name, station_lat, station_lng)