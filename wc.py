from woocommerce import API
from settings import CONSUMER_KEY, CONSUMER_SECRET, WEBSITE_URL, IMAGGA_API_KEY, IMAGGA_API_SECRET
from bs4 import BeautifulSoup
from math import *
import requests


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
    image_src = []

    for image in images:
        image_src.append(image["src"])

    return image_src


def get_tags_by_image(product_id, language="en"):
    response = requests.get(
        f'https://api.imagga.com/v2/tags?image_url=%s&language={language}' % get_image_url(product_id)[0],
        auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET))

    image_tags = response.json()["result"]["tags"]

    return image_tags


def get_colors(product_id):
    image_url = get_image_url(product_id)
    response = requests.get(
        'https://api.imagga.com/v2/colors?image_url=%s' % image_url[0],
        auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET))

    colors = response.json()["result"]["colors"]["image_colors"]
    # for predicted_color in colors:
    #     print(round(predicted_color["percent"], 2), "% : ", predicted_color["closest_palette_color"])
    return colors

def auth_product(product_id, language=""):
    time_out = 20
    language = language + "/"
    api_code = f"{language}wc-api/v3/"
    response = requests.get(
        f"{WEBSITE_URL}{api_code}products/{product_id}?consumer_key={CONSUMER_KEY}&consumer_secret={CONSUMER_SECRET}",
        timeout=time_out
    )
    return response


def get_title_json(product_id, language=""):
    response = auth_product(product_id, language)
    title = response.json()["product"]["title"]
    return title


def get_description(product_id, language=""):
    response = auth_product(product_id, language)
    description_html = response.json()["product"]["description"]

    clean_description = clean_html(description_html)
    return clean_description


def clean_html(html_code):
    # clean up HTML #

    clean_text = BeautifulSoup(html_code, "lxml").text
    return clean_text


def get_title(product_id, language=""):
    respond = requests.get(f"{WEBSITE_URL}{language}/product/?p={product_id}").content
    soup = BeautifulSoup(respond, 'html.parser')
    title = soup.select('h1.product_title')[0].text.strip()
    return title


def get_tags(product_id, language="en"):
    tags = []

    for tag in get_tags_by_image(product_id, language):
        new_tag = {
            "name": tag["tag"][f"{language}"],
            "confidence": floor(tag["confidence"])
        }
        tags.append(new_tag)

    return tags


def list_all_products():
    global wcapi
    page = 1
    product_list = []
    per_page_item = 100  # 1 to 100

    products = wcapi.get(f"products?per_page={per_page_item}&page={page}").json()

    while products:
        if products:
            for p in products:
                name_en = get_title(p["id"], "en")
                product_list.append([p["id"], p["sku"], p["name"], name_en])
                print(product_list[-1])

        page += 1
        products = wcapi.get(f"products?per_page={per_page_item}&page={page}").json()

    return product_list


def save_all_products():
    all_products = list_all_products()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for p in all_products:
            product_id = p[0]
            sku = p[1]
            product_name = p[2]
            product_name_en = p[3]
            f.write(f"{product_id},{sku},{product_name},{product_name_en}\n")


def get_filtered_products():
    respond = requests.get(WEBSITE_URL)
    print(respond)
