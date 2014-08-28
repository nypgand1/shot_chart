import json

FILE_NAME_CENTER_8 = './center.json'
FILE_NAME_OUTPUT = 'shoppingMall.json'

NUM_POINTS = 64


def convertor_to_xy(filename):
    
    zone_xy = list()
    
    with open(filename) as f:
        poly = json.load(f)
    
        xy = poly['xy']
    
        xy_len = len(xy)
        step = xy_len / NUM_POINTS
    
        for i in range(0, xy_len, step):
            print i
            print xy[i]
            print xy[i+1]
            print '\n'
    
            zone_xy.append([xy[i], xy[i+1]])

    return zone_xy


zone_center_8 = dict()
zone_center_8['geometry'] = {'type': 'Polygon', 'coordinates': [convertor_to_xy(FILE_NAME_CENTER_8)]}
zone_center_8['properties'] = {"ID": "0", "ShopName": "center_8"}

features = list()
features.append(zone_center_8)

print json.dumps(zone_center_8, indent=4, separators=(',', ': '))


with open(FILE_NAME_OUTPUT) as f:
    output = json.load(f)
    output['features'] = features


with open(FILE_NAME_OUTPUT, 'w') as f:
    json.dump(output, f, indent=4, separators=(',', ': '))

