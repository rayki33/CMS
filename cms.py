import mysql.connector

HOST = "192.72.212.142"
PORT = "3306"
DATABASE = "open3ame"
USER = "open3ame"
PASSWORD = "dkHtzKRCX2kHcMyE"


class ContentManager():
    def __init__(self):
        self.name = "Content Manager"
        recordset = 0

    def connect_to_database(self):
        self.mydb = mysql.connector.connect(
            host=HOST,
            # port=PORT,
            database=DATABASE,
            user=USER,
            password=PASSWORD

        )
        print("Database is successfully connected.")
        return True

    def success(self):
        print("success!")

