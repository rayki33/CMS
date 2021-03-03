import mysql.connector

HOST = "192.72.212.142"
PORT = "3306"
DATABASE = "open3ame"
USER = "open3ame"
PASSWORD = "dkHtzKRCX2kHcMyE"



# SQL
# Create table

# CREATE_ORDER_TABLE = "CREATE TABLE order(id INT AUTO_INCREMENT PRIMARY KEY, " \
#                      "order_date DATE, " \
#                      "account CHAR, " \
#                      "order_num CHAR " \
#                      "amount FLOAT, " \
#                      "currency CHAR, " \
#                      "shipping_method CHAR, " \
#                      "recipient CHAR, " \
#                      "shipping_address CHAR, " \
#                      "shipping_country CHAR, " \
#                      "tel CHAR(15))"

CREATE_ORDER_TABLE = "CREATE TABLE orders(" \
                     "id INT AUTO_INCREMENT PRIMARY KEY, " \
                     "order_id VARCHAR(15), " \
                     "store_id INT(11) , " \
                     "amount DECIMAL(15,4), " \
                     "currency VARCHAR(3), " \
                     "shipping_id INT(11))"

CREATE_ORDER_SHIPPING_TABLE = ""

ADD_NEW_CUSTOMER = "INSERT INTO customers (name, address) VALUE ('Carl','XYZ cr Hong Kong')"

def connect():
    database_name = mysql.connector.connect(
        host=HOST,
        # port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )
    return database_name

#
# class Database():
#     def __init__(self):
#
#         self.name = "Content Manager"
#         recordset = 0
#
#         self.mydb = mysql.connector.connect(
#             host=HOST,
#             # port=PORT,
#             database=DATABASE,
#             user=USER,
#             password=PASSWORD
#         )
#
#         self.cursor = self.mydb.cursor()
#         self.commit = self.mydb.commit()
#
#     def show_table(self):
#         self.cursor.execute("SHOW TABLES")
#         print("Show all tables.")
#
#     def create_table(self, table_name):
#         self.cursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#
#     def execute(self, sql):
#         self.cursor.execute(sql)