from woocommerce import API
import pandas as pd
import openpyxl

consumer_key = "ck_119365fc642a9129cfaadf213f8bace06c623c9f"
consumer_secret = "cs_fea9c7552cf3cba6a590172ae8c02700e63cb2c7"


wcapi = API(
    url="https://www.thecsdesign.com",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    wp_api=True,
    version="wc/v3"
)

data_json = wcapi.get("products").json()
# print(data_json)
wp_products = pd.DataFrame(data_json)
# print(wp_products[{"name", "sku", "description", "images"}])
# wp_products[{"name", "sku", "description", "images"}].to_excel('./export/wp_product.xlsx')


product = wp_products.loc[8]
print(product)


images = product['images']
for image in images:
    print(image['src'])