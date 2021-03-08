from woocommerce import API
from settings import CONSUMER_KEY, CONSUMER_SECRET, WEBSITE_URL
from bs4 import BeautifulSoup
from math import *

wcapi = API(
    url="https://www.thecsdesign.com",
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    wp_api=True,
    version="wc/v3",
    timeout=20
)

def get_image_url(product_id):
    data = wcapi.get(f'products/{product_id}').json()

    images = data["images"]
    image = images[0]["src"]
    image_src = []

    for image in images:
        image_src.append(image["src"])

    return image_src

import requests

api_key = 'acc_0dd6492e5c12fae'
api_secret = '7af065628a007809449698cc5cdf74f3'


def get_tags_by_image(product_id):
    ## tags ##
    global api_key, api_secret, image_url
    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % get_image_url(product_id)[0],
        auth=(api_key, api_secret))

    image_tags = response.json()["result"]["tags"]

    return image_tags

    # for tag in image_tags:
    #     print(tag["tag"])


def color():
    ## color ##
    global api_key, api_secret, image_url
    response = requests.get(
        'https://api.imagga.com/v2/colors?image_url=%s' % image_url,
        auth=(api_key, api_secret))

    colors = response.json()["result"]["colors"]["image_colors"]
    for color in colors:
        print(round(color["percent"], 2), "% : ", color["closest_palette_color"])


def auth_product(product_id, language=""):
    time_out = 20
    language = language + "/"
    api_code = f"{language}wc-api/v3/"
    id = product_id
    response = requests.get(
        f"{WEBSITE_URL}{api_code}products/{id}?consumer_key={CONSUMER_KEY}&consumer_secret={CONSUMER_SECRET}", timeout=time_out
    )
    return response


def get_title_json(product_id, language=""):
    response = auth_product(product_id, language)
    title = response.json()["product"]["title"]
    return (title)


def get_description(product_id, language=""):
    response = auth_product(product_id, language)
    description_html = response.json()["product"]["description"]

    clean_description = clean_html(description_html)
    return (clean_description)


def clean_html(html_code):
    ## clean up HTML ##


    clean_text = BeautifulSoup(html_code, "lxml").text
    return clean_text



def get_title(product_id, language = ""):
    respond = requests.get(f"{WEBSITE_URL}{language}/product/?p={product_id}").content
    soup = BeautifulSoup(respond, 'html.parser')
    title = soup.select('h1.product_title')[0].text.strip()
    return title


def get_tags(product_id):

    tags = []

    for tag in get_tags_by_image(product_id):
        new_tag = {
            "name": tag["tag"]["en"],
            "confidence": floor(tag["confidence"])
        }
        tags.append(new_tag)

    return tags


# print(get_title(3042,"en"))
# for tag in get_tags(3042):
#     if tag['confidence'] > 20:
#         print(tag['name'], ":", tag['confidence'])

def list_all_products():
    global wcapi
    page = 1
    all_products = []

    products = wcapi.get(f"products?per_page=100&page={page}").json()
    for product in products:
        all_products.append([product["id"], product["name"]])

    return all_products

print(list_all_products())