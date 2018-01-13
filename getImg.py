# img scraping from unpslash

import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://unsplash.com/collections/1521669/editors-choice-2017-photos-of-the-year'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#locate all elements with img tag
image_tags = soup.findAll('img')

# create directory for images
if not os.path.exists('imgs'):
	os.makedirs('imgs')

#move to new directory
os.chdir('imgs')

#img file name var
x = 0

#write images
for image in image_tags:
	try:
		url = image['src']
		response = requests.get(url)
		if response.status_code == 200:
			with open('img-' + str(x) + '.jpg', 'wb') a f:
				f.write(requests.get(url).content)
				f.close()
				x += 1
	except:
		pass