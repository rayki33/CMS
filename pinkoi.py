import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Select action')
parser.add_argument("-updatephone", "--updatePhoneListing", action="store_true", help="update listing with phone model")

args = parser.parse_args()


def read_csvfile(datafile):
    data = pd.read_csv(datafile)
    datasets = data.to_numpy()
    return datasets


# Update Pinkoi Listing
if args.updatePhoneListing:
    phones = read_csvfile('data/phone-glossy.csv')
    listings = read_csvfile('data/pinkoi-listing-phonecase-glossy-tpu-all.csv')

    from modules.pinkoi.UpdateListing import *
    update_listing(listings, phones)

else:
    print("No argument selected!")
