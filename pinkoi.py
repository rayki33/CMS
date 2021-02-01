import chardet
import pandas as pd


class Pinkoi:
    def __init__(self):
        pass

    def read_order_csv(self, csv_filename):
        # read order csv file

        with open(csv_filename,'rb') as f:
            result = chardet.detect(f.read())
            df = pd.read_csv(csv_filename, encoding=result['encoding'], sep='\t', quotechar='"')
        return df


    #todo: login
    #todo: order handling
    #todo: download orders in csv format
    #todo: save ONLY orders that are not found in database
    #todo: check whether the order exists in the database
    #todo: check element location exist

