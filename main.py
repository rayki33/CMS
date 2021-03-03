from pinkoi import Pinkoi
from wordpress import Wordpress
from settings import WP_PRODUCT_CSV, PK_ORDERS_CSV

pk = Pinkoi()
wp = Wordpress()


orders = pk.read_csv(PK_ORDERS_CSV)
print(orders['訂單編號'])





