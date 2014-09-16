import json

FILE_NAME_INPUT = list()
FILE_NAME_INPUT.append('./zone/center_08.json')

FILE_NAME_INPUT.append('./zone/center_08_16.json')
FILE_NAME_INPUT.append('./zone/left_08_16.json')
FILE_NAME_INPUT.append('./zone/right_08_16.json')
FILE_NAME_INPUT.append('./zone/center_16_24.json')
FILE_NAME_INPUT.append('./zone/left_16_24.json')
FILE_NAME_INPUT.append('./zone/right_16_24.json')
FILE_NAME_INPUT.append('./zone/left_center_16_24.json')
FILE_NAME_INPUT.append('./zone/right_center_16_24.json')

FILE_NAME_INPUT.append('./zone/center_24.json')
FILE_NAME_INPUT.append('./zone/left_24.json')
FILE_NAME_INPUT.append('./zone/right_24.json')
FILE_NAME_INPUT.append('./zone/left_center_24.json')
FILE_NAME_INPUT.append('./zone/right_center_24.json')

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

for filename in FILE_NAME_INPUT:
    zone_xy, center_xy = convert_to_xy(filename)

    zone = dict()
    zone['geometry'] = {'type': 'Polygon', 'coordinates': zone_xy, 'center':center_xy}
    zone['properties'] = {'ID': len(features), 'zone_name': filename}
    features.append(zone)

    #print json.dumps(zone, indent=4, separators=(',', ': '))


with open(FILE_NAME_OUTPUT) as f:
    output = json.load(f)
    output['features'] = features


with open(FILE_NAME_OUTPUT, 'w') as f:
    json.dump(output, f, indent=4, separators=(',', ': '))

