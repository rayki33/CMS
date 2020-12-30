import argparse
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser(description='Select action')
parser.add_argument("-ul","--updatelisting", action="store_true",help="update pinkoi listing with phone model")

args = parser.parse_args()


def read_csvfile(datafile):
    data = pd.read_csv(datafile)
    datasets = data.to_numpy()
    # datasets = data.to_records()

    return datasets


# Update Pinkoi Listing
if args.updatelisting:
    phones = read_csvfile('data/phone-glossy.csv')
    listings = read_csvfile('data/pinkoi-listing.csv')

    from modules.UpdateListing import *
    update_listing(listings,phones)
