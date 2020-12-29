import argparse
import pandas as pd
import numpy as np


parser = argparse.ArgumentParser(description='Select action')
parser.add_argument("-ul","--updatelisting", action="store_true",help="update pinkoi listing with phone model")

args = parser.parse_args()

# Main Control Panel

# listingIDs = ["nX9CVcNN","CbvfPDvU","ChBY3sbx","Eu49t7gP","YGgWmwZU","nHJY2j5K","jNFfitCp","NDxRTAqW","GJg52cPf","TtvA7GuC","s46b6gcs","J7uEvAgB","vgfZpFfH","85PvKjmm","Z2Lxnqqj","JcnwvWkn","Ew8FnhfG","kaM6VxAU"]
# SKUs = ["PCAM95A","PCAM24B","PCAM24A","PCAM06E","PCAM06C","PCAM06B","PCAM06A","PCAM84D","PCAM84B","PCAM84A","PCAM35A","PCAM02B","PCAM89H","PCAM89E","PCAM89D","PCAM89C","PCAM89B","PCAM89A"]

# listingIDs_1 = ["C6z2hhXK","N8tf5Tnw","n8S7bmrc","VUVCUjWC","QzWRg7PW","qYXKNEZn","mFZuQb7F","pFMpqHZG","zbrWzt6J","kSUcBDzG","QK9sKwQP","jRDWQSma","7hc5Bnbf","y8HAy5pz","b7nXksJY","Wy7bPhhh","5PT2Kv7X","VE3wCc5w","9rHungKs","6WeZumKT","TQwPU2ae","z9NqHNgk","6TAQ2UiZ","aP4fgqET","REDHqgxH","RfWhA5Qu","jWxYnYHS","733JxjOu","3tU4CN5a","rWykgiWY","zbMdeimq"]
# SKUs_1 = ["PCGS-PL-01","PCAM95Q","PCAM95P","PCAM95O","PCJN36-3","PCAM95L","PCAM99I","PCAM99H","PCAM99G","PCAM99J","PCAM99E","PCAM100F","PCAM100D","PCAM100C","PCAM100B","PCAM99D","PCAM99C","PCAM99B","PCAM99A","PCJN47-2","PCJN45-3","PCJN45-2","PCJN45-1","PCJN42-4","PCJN42-3","PCTP-AM89B","PCTP-JN42-3","PCTP-AM19A","PCTP-AM44A1","PCTP-AM44B1","PCTP-AM44A"]

listingIDs = ["Av9FX5f4","H6sLvJ6b","k6sPT4V9","fC467hxc","mnuTvJcB","bre7NZJr","J4rbCsCC","cVhWVyRU","gKBDAwqS","fjZwLbVc"]
SKUs = ["PCTP-AM41H","PCTP-AM41D","PCTP-AM41E","PCTP-AM41F","PCTP-AM41B","PCTP-AM89C","PCTP-AM89H","PCTP-AM89E","PCTP-AM89F","PCTP-AM89D"]


# phones = ["iPhone 12 mini","iPhone 12 Pro Max","iPhone 12 Pro","iPhone SE 2020"]



# Update Pinkoi Listing
if args.updatelisting:
    from modules.UpdateListing import *
    update_listing(listingTPU7,skuTPU7,phonescase_glossy)

dataPhone = pd.read_csv('data/phone-glossy.csv')
# print(data.loc[0])
dataPhones = dataPhone.to_numpy()
# print(dataPhones)


dataListing = pd.read_csv('data/pinkoi-listing.csv')
# print(data.loc[0])
dataListings = dataListing.to_numpy()
print(dataListings)
