try:
 import unzip_requirements
except ImportError:
 pass

import json
import pandas as pd
from pandas.io.json import json_normalize
from matplotlib import path

df = pd.read_json('https://www.had.gov.hk/psi/hong-kong-administrative-boundaries/hksar_18_district_boundary.json')
districts = json_normalize(df['features'])

def check_hk_district(latitude, longitude):
    # format in GML: longitude, latitude
    poi = [longitude, latitude]

    for ind, district in districts.iterrows():
        district_path = path.Path(district['geometry.coordinates'][0])
        district_name = district['properties.District']
        if district_path.contains_point(poi):
            return district_name
    return 'Nil'

def main(event, context):
    if 'latitude' in event and 'longitude' in event:
        lati = event['latitude']
        longi = event['longitude']

        try:
            res = check_hk_district(lati, longi)
            return {
                'statusCode': 200,
                'body': json.dumps(res)
            }
        except TypeError:
            return {
                'statusCode': 400,
                'body': json.dumps('latitude or longitude is not a float')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('latitude or longitude not found in input')
        }

if __name__ == '__main__':
    event = {"latitude": 22.529967, "longitude": 114.145680}
    print(main(event, ''))