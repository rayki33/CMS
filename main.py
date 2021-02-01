from cms import ContentManager
from pinkoi import Pinkoi
from wordpress import Wordpress

cms = ContentManager()
pk = Pinkoi()
wp = Wordpress()




#
# csv_filename = "data/pinkoi-orders-csdesign.csv"
# wp_file = "data/wc-product-export-1-2-2021-1612170067228.csv"
# # orders = pinkoi.read_order_csv(csv_filename)
# products = wp.read_product_csv(wp_file)
#
# # print(products)
# print(products.iloc[0][8])
#
# # for order in range(len(orders)):
# #     print(orders.iloc[order][4])