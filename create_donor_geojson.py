import json
import pandas as pd

dtype_dict = {'zipcode': str, 'PCT_DONORS': 'float'}
zip_donors_df = pd.read_csv('donor_data_map.csv', dtype=dtype_dict)
tmp_donors = zip_donors_df.set_index('zipcode').to_dict()
zip_donors = tmp_donors['PCT_DONORS']

with open('nyc_zips.json') as file:
  zips = json.load(file)

# zips['features'][0]['properties']['density'] = 22.5

for feature in zips['features']:
  current_zip = feature['properties']['postalCode']
  if current_zip in zip_donors:
    feature['properties']['density'] = zip_donors[current_zip] * 100

with open('nyc_zips_with_donor.json', 'w') as file:
  json.dump(zips, file)