import json

FILE_NAME_INPUT = dict()
FILE_NAME_INPUT['center_08'] = './zone/center_08.json'
FILE_NAME_INPUT['center_08_16'] = './zone/center_08_16.json'
FILE_NAME_INPUT['center_16_24'] = './zone/center_16_24.json'
FILE_NAME_INPUT['center_24'] = './zone/center_24.json'
FILE_NAME_INPUT['left_08_16'] = './zone/left_08_16.json'
FILE_NAME_INPUT['left_16_24'] = './zone/left_16_24.json'
FILE_NAME_INPUT['left_24'] = './zone/left_24.json'
FILE_NAME_INPUT['left_center_16_24'] = './zone/left_center_16_24.json'
FILE_NAME_INPUT['left_center_24'] = './zone/left_center_24.json'
FILE_NAME_INPUT['right_08_16'] = './zone/right_08_16.json'
FILE_NAME_INPUT['right_16_24'] = './zone/right_16_24.json'
FILE_NAME_INPUT['right_24'] = './zone/right_24.json'
FILE_NAME_INPUT['right_center_16_24'] = './zone/right_center_16_24.json'
FILE_NAME_INPUT['right_center_24'] = './zone/right_center_24.json'


FILE_NAME_OUTPUT = 'shot_chart_zone.json'


def convert_to_xy(filename):
    
    zone_xy = list()
    
    with open(filename) as f:
        poly = json.load(f)
        xy = poly['xy']
        xy_len = len(xy)
    
        for i in range(0, xy_len, 2):
            zone_xy.append([xy[i], xy[i+1]])

    return zone_xy


features = list()

for name, filename in FILE_NAME_INPUT.iteritems():
    zone = dict()
    zone['geometry'] = {'type': 'Polygon', 'coordinates': [convert_to_xy(filename)]}
    zone['properties'] = {'ID': len(features), 'ShopName': name}
    features.append(zone)

    #print json.dumps(zone, indent=4, separators=(',', ': '))


with open(FILE_NAME_OUTPUT) as f:
    output = json.load(f)
    output['features'] = features


with open(FILE_NAME_OUTPUT, 'w') as f:
    json.dump(output, f, indent=4, separators=(',', ': '))

