from woocommerce import API
from settings import CONSUMER_KEY, CONSUMER_SECRET, WEBSITE_URL
from bs4 import BeautifulSoup

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

# print(name)

images = data["images"]
# for image in images:
# print(image["src"])

image_1 = images[0]["src"]
# print(image_1)

import requests

api_key = 'acc_0dd6492e5c12fae'
api_secret = '7af065628a007809449698cc5cdf74f3'
image_url = image_1


def tags():
    ## tags ##
    global api_key, api_secret, image_url
    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(api_key, api_secret))

    image_tags = response.json()["result"]["tags"]
    print(image_tags[0], image_tags[1])

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


def title(product_id, language=""):
    response = auth_product(product_id, language)
    title = response.json()["product"]["title"]
    return (title)


def description(product_id, language=""):
    response = auth_product(product_id, language)
    description_html = response.json()["product"]["description"]

    clean_description = clean_html(description_html)
    return (clean_description)


def clean_html(html_code):
    ## clean up HTML ##


    clean_text = BeautifulSoup(html_code, "lxml").text
    return clean_text


# print(title(3134, "en"))
# print(description(3134,"en"))

def get_english_title():
    respond = requests.get("https://www.thecsdesign.com/en/product/?p=3134").content

    soup = BeautifulSoup(respond, 'html.parser')

    title_html = soup.find_all('h1', attrs={'class': 'product_title'})[0]
    # title = BeautifulSoup(title_html[0], "lxml").text

    return title_html

print(get_english_title())