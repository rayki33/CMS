from contentmanager import ContentManager
from pinkoi import Pinkoi
from wordpress import Wordpress

import database as db
mydb = db.connect()
cursor = mydb.cursor()

def db_test():
    cursor.execute("DROP TABLE orders")
    cursor.execute(db.CREATE_ORDER_TABLE)
    mydb.commit()
    mydb.close()


pk = Pinkoi()
wp = Wordpress()

# wp_product_file = "data/wc-product-export-1-2-2021-1612170067228.csv"

PK_ORDERS = "data/pinkoi-orders-csdesign.csv"

pk_orders = pk.read_order_csv(PK_ORDERS)
for order in range(len(pk_orders)):
    print(pk_orders.iloc[order][4])

