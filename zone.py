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
    center_xy = [0, 0]
    
    with open(filename) as f:
        poly = json.load(f)
        xy = poly['xy']
        xy_len = len(xy)
    
        for i in range(0, xy_len, 2):
            zone_xy.append([xy[i], xy[i+1]])
            center_xy[0] = center_xy[0] + xy[i]
            center_xy[1] = center_xy[1] + xy[i+1]

    center_xy[0] = center_xy[0] / (xy_len/2)
    center_xy[1] = center_xy[1] / (xy_len/2)

    return zone_xy, center_xy


features = list()

for name, filename in FILE_NAME_INPUT.iteritems():
    zone_xy, center_xy = convert_to_xy(filename)

    zone = dict()
    zone['geometry'] = {'type': 'Polygon', 'coordinates': zone_xy, 'center':center_xy}
    zone['properties'] = {'ID': len(features), 'zone_name': name}
    features.append(zone)

    #print json.dumps(zone, indent=4, separators=(',', ': '))


with open(FILE_NAME_OUTPUT) as f:
    output = json.load(f)
    output['features'] = features


with open(FILE_NAME_OUTPUT, 'w') as f:
    json.dump(output, f, indent=4, separators=(',', ': '))

