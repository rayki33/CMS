from woocommerce import API
from settings import CONSUMER_KEY, CONSUMER_SECRET

wcapi = API(
    url="https://www.thecsdesign.com",
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    wp_api=True,
    version="wc/v3",
    timeout=10
)

product_id = 2593
data = wcapi.get(f'products/{product_id}', params={"lang": "en"}).json()

name = data["name"]
description = data["description"]

print(name)

images = data["images"]
# for image in images:
    # print(image["src"])

image_1 = images[0]["src"]
print(image_1)

import requests

api_key = 'acc_0dd6492e5c12fae'
api_secret = '7af065628a007809449698cc5cdf74f3'
image_url = image_1

## tags ##
response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

image_tags = response.json()["result"]["tags"]
print(image_tags[0],image_tags[1])

# for tag in image_tags:
#     print(tag["tag"])


## color ##
response = requests.get(
    'https://api.imagga.com/v2/colors?image_url=%s' % image_url,
    auth=(api_key, api_secret))

colors = response.json()["result"]["colors"]["image_colors"]
for color in colors:
    print(round(color["percent"], 2),"% : ", color["closest_palette_color"])


## clean up HTML ##
# from bs4 import BeautifulSoup
#
# clean_description = BeautifulSoup(description, "lxml").text
# print(clean_description)
