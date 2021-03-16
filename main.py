from pinkoi import Pinkoi
from wordpress import Wordpress
from settings import WP_PRODUCT_CSV, PK_ORDERS_CSV

from wc import *

print(get_title(2510, "en"))
#
# for tag in get_tags(2510):
#     if tag["confidence"] > 10:
#         print(tag["name"])

# print(color(2510))
# print(get_tags_by_image(2510, "zh_cht"))
tags = (get_tags(2510, "zh_cht"))
for tag in tags:
    if tag["confidence"] > 15:
        print(tag["name"])