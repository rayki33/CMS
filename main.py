from cms import ContentManager
from pinkoi import Pinkoi

cms = ContentManager()
pinkoi = Pinkoi()

csv_filename = "data/pinkoi-orders-csdesign.csv"
orders = pinkoi.read_order_csv(csv_filename)

for order in range(len(orders)):
    print(orders.iloc[order][4])