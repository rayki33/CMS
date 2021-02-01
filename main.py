from cms import ContentManager
from pinkoi import Pinkoi
from wordpress import Wordpress

cms = ContentManager()
pk = Pinkoi()
wp = Wordpress()


pk_order_file = "data/pinkoi-orders-csdesign.csv"
wp_product_file = "data/wc-product-export-1-2-2021-1612170067228.csv"

products = wp.read_product_csv(wp_product_file)


print(products)
print(products.iloc[0])

# # for order in range(len(orders)):
# #     print(orders.iloc[order][4])