import json

FILE_NAME_INPUT = {'center_8': './zone/center_8.json', 'center_8_16': './zone/center_8_16.json'}
FILE_NAME_OUTPUT = 'shot_chart_zone.json'


def convert_to_xy(filename):
    
    zone_xy = list()
    
    with open(filename) as f:
        poly = json.load(f)
        xy = poly['xy']
        xy_len = len(xy)
    
        for i in range(0, xy_len, 2):
            print i
            print xy[i]
            print xy[i+1]
            print '\n'
    
            zone_xy.append([xy[i], xy[i+1]])

    return zone_xy


features = list()

for name, filename in FILE_NAME_INPUT.iteritems():
    zone = dict()
    zone['geometry'] = {'type': 'Polygon', 'coordinates': [convert_to_xy(filename)]}
    zone['properties'] = {'ID': len(features), 'ShopName': name}
    features.append(zone)

    print json.dumps(zone, indent=4, separators=(',', ': '))


with open(FILE_NAME_OUTPUT) as f:
    output = json.load(f)
    output['features'] = features


with open(FILE_NAME_OUTPUT, 'w') as f:
    json.dump(output, f, indent=4, separators=(',', ': '))

