from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs4

# settings to initialize BeautifulSoup and open the website
site = 'http://startupguide.nyc/'
header = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers = header)
page = urlopen(req)

# read the site and store all 'a' tags
soup = bs4(page, 'html.parser')
name_box = soup.find_all('a', target="_blank")

# function to write to file
def write_to_file(data):
  with open('businesses.txt', 'a') as file:
    file.write(data)
    file.write('\n')

# we want first 116
for link in name_box:
  write_to_file(link.get('href'))