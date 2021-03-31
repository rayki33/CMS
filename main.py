import pandas as pd
from carousell import *
from wc import *

def main(product_id):
    # print(get_title(product_id, "zh"))
    tags = (get_tags(product_id, "zh_cht"))
    # for tag in tags:
    #     if tag["confidence"] > 30:
    #         print(tag)
    for color in get_colors(product_id):
        color_parents = color["closest_palette_color_parent"]
        print(color_parents)

# main(2230)
# data = pd.read_csv("data/no_attribute_product.txt").to_dict(orient="list")["product_id"]

def main_carousell(product_id):
    cs = Carousell()
    cs.sell(product_id)

main_carousell(2230)