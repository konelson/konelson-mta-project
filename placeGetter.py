import googlemaps
gmaps = googlemaps.Client(key='')

# function to write to file
def write_to_file(name, place_zip):
  with open('businesses_zips.txt', 'a') as file:
    file.write(name + ' ' + place_zip)
    file.write('\n')

# use gmaps api to retrieve address and pull zip out
def get_zip(name):
  current_place_data = gmaps.places(name + " new york")
  results = current_place_data['results']

  if results:
    current_place_text = current_place_data['results'][0]['formatted_address']  
    string_pos_base = current_place_text.find("USA")
  
    # grab the right position within the string to get the zip 
    string_pos_1 = string_pos_base - 7
    string_pos_2 = string_pos_base - 2
    current_place_zip = current_place_text[string_pos_1:string_pos_2]
  else:
    current_place_zip = '0'
  
  return current_place_zip

# parse the URL and retrieve the "name"
def get_name_from_url(url):
  end_pointer = url.rfind(".")
  beg_pointer = url.find(".")

  if end_pointer == beg_pointer:
    beg_pointer = url.find("/") + 2
  else:
    beg_pointer += 1

  return url[beg_pointer:end_pointer]

# read the first 116 lines of the scraped business data
file = open("businesses.txt", "r")
business_url_data = file.readlines()

i = 0
while i <= 116:
  name = get_name_from_url(business_url_data[i])
  print('working on ' + name + '...')
  zip_code = get_zip(name)
  write_to_file(name, zip_code)
  i += 1