import json
import G15DatasetStop
import G15DatasetRoute
from geopy.distance import geodesic
#pip install geopy

origin = (51.444476, 5.4793668) #EhvCentraal
dist = (51.4329456, 5.4653846)  #BusStop EhvMecklenburgstraat

f = open('BusStopsEhvGeoJson.json', 'r', encoding='utf-8')
result = G15DatasetStop.bus_stop_ehv_from_dict(json.loads(f.read()))

print(len(result.elements))

f = open('BusRoutesEhvGeoJson.json', 'r', encoding='utf-8')
result = G15DatasetRoute.bus_route_ehv_from_dict(json.loads(f.read()))

print(len(result.features))
