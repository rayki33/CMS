import chardet
import pandas as pd

class Wordpress:
    def __init__(self):
        pass

    def read_csv(self, csv_file):
        # read order csv file
        with open(csv_file, 'rb') as f:
            result = chardet.detect(f.read())
            df = pd.read_csv(csv_file, encoding=result['encoding'])
        return df