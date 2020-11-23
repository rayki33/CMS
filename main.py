from UpdateListing import *

# Main Control Panel

# listingIDs = ["nX9CVcNN","CbvfPDvU","ChBY3sbx","Eu49t7gP","YGgWmwZU","nHJY2j5K","jNFfitCp","NDxRTAqW","GJg52cPf","TtvA7GuC","s46b6gcs","J7uEvAgB","vgfZpFfH","85PvKjmm","Z2Lxnqqj","JcnwvWkn","Ew8FnhfG","kaM6VxAU"]
# SKUs = ["PCAM95A","PCAM24B","PCAM24A","PCAM06E","PCAM06C","PCAM06B","PCAM06A","PCAM84D","PCAM84B","PCAM84A","PCAM35A","PCAM02B","PCAM89H","PCAM89E","PCAM89D","PCAM89C","PCAM89B","PCAM89A"]

# listingIDs_1 = ["C6z2hhXK","N8tf5Tnw","n8S7bmrc","VUVCUjWC","QzWRg7PW","qYXKNEZn","mFZuQb7F","pFMpqHZG","zbrWzt6J","kSUcBDzG","QK9sKwQP","jRDWQSma","7hc5Bnbf","y8HAy5pz","b7nXksJY","Wy7bPhhh","5PT2Kv7X","VE3wCc5w","9rHungKs","6WeZumKT","TQwPU2ae","z9NqHNgk","6TAQ2UiZ","aP4fgqET","REDHqgxH","RfWhA5Qu","jWxYnYHS","733JxjOu","3tU4CN5a","rWykgiWY","zbMdeimq"]
# SKUs_1 = ["PCGS-PL-01","PCAM95Q","PCAM95P","PCAM95O","PCJN36-3","PCAM95L","PCAM99I","PCAM99H","PCAM99G","PCAM99J","PCAM99E","PCAM100F","PCAM100D","PCAM100C","PCAM100B","PCAM99D","PCAM99C","PCAM99B","PCAM99A","PCJN47-2","PCJN45-3","PCJN45-2","PCJN45-1","PCJN42-4","PCJN42-3","PCTP-AM89B","PCTP-JN42-3","PCTP-AM19A","PCTP-AM44A1","PCTP-AM44B1","PCTP-AM44A"]

listingIDs = ["Av9FX5f4","H6sLvJ6b","k6sPT4V9","fC467hxc","mnuTvJcB","bre7NZJr","J4rbCsCC","cVhWVyRU","gKBDAwqS","fjZwLbVc"]
SKUs = ["PCTP-AM41H","PCTP-AM41D","PCTP-AM41E","PCTP-AM41F","PCTP-AM41B","PCTP-AM89C","PCTP-AM89H","PCTP-AM89E","PCTP-AM89F","PCTP-AM89D"]

phonescase_glossy = ["iPhone 12 mini","iPhone 12 Pro Max","iPhone 12 Pro","iPhone 12","iPhone SE 2020","iPhone 11 Pro Max","iPhone 11 Pro","iPhone 11","iPhone XS Max","iPhone XS","iPhone XS Max","iPhone XR","iPhone X","iPhone 8 Plus","iPhone 8","iPhone 7 Plus","iPhone 7","iPhone 6","iPhone 6s","iPhone 6 Plus","iPhone 6s Plus","Samsung S20+","Samsung S20 Ultra 5G","Samsung S20 FE 5G","Samsung S20","Samsung S10e","Samsung S10 Plus","Samsung S10 Lite","Samsung S10","Samsung S9 Plus","Samsung S9","Samsung Note 20 Ultra 5G","Samsung Note 20","Samsung Note 10 Lite","Samsung Note 10","Samsung Note 9","Samsung Note 8","Samsung A80","Samsung A71","Samsung A70","Samsung A60","Samsung A51","Samsung A50s","Samsung A40s","Samsung A31","Xiaomi 10","Xiaomi 10 Pro","Redmi K30 Pro","Huawei P20","Huawei P20 Lite","Huawei P20 Pro","Huawei P30","Huawei P30 Pro","Huawei P30 Lite","Huawei P40","Huawei P40 Pro","Huawei P40 Pro +","Huawei Y6P","Huawei Y6S","Huawei Y9S","Huawei Mate 20","Huawei Mate 20 Pro","Huawei Mate 20 X","Huawei Mate 30 Pro","Huawei Nova 7","Huawei Nova 7 SE","其他型號請聯絡客服"]
# phones = ["iPhone 12 mini","iPhone 12 Pro Max","iPhone 12 Pro","iPhone SE 2020"]


listing_TPU1 =["dqezb5Ar","gJT7qDKd","4GfTUgMa","yz3CPL8R","KphtPSyY","cy8XGQnY","kFQsGs6x","EzwwhnGB","p7i95fmp","VcA7HZ4w","bXESkLJU","eP9C8J65"]
SKU_TPU1 = ["PCTP-JN17-2","PCTP-PCJN06-1","PCTP-AM64C","PCTP-AM68B","PCTP-JN33-7","PCTP-JN36-4","PCTP-JN21-5","PCTP-JN33-2","PCTP-JN36-2","PCTP-JN36-1","PCTP-JN36-3","PCTP-JN24-4"]

listing_TPU2 =["iF8stfpD","LMnnzfAx","mdB2pN5a","jTR7yH9Q","B36QRALN","zgig8eZw","C4L3bfAf","XjwkxLvJ","rDZsvXmd","5e8QyeRj","Cd8za64y","RbBDURWk"]
SKU_TPU2 = ["PCTP-JN33-4","PCTP-JN47-3","PCTP-JN21-4","PCTP-JN40-3","PCTP-JN40-1","PCTP-AM100-1","PCTP-AM100-2","PCTP-AM100-3","PCTP-JN38-2","PCTP-JN21-1","PCTP-JN21-3","PCTP-JN21-2"]

listingTPU5 = ["YEvGyH4k","PGaYgJYJ","tXEA4SCx","IDYzz8fe","37XG3PfP","5nRIPe2b","YcCdj385","hbeQAfNY","DwCD8fg3","68qMkhbT","9buZb3d3","UMmJMei2","KXSyv4g5","9462EtKk","EQwBTgEP","NeFTMajN","fs2NECSP","u9P7WBZa","E3VddsJb","XjwkxLvJ","6vR3E6u8","RbBDURWk"]
skuTPU5 = ["PCTP-AM1-03","PCTP-AM68A","PCTP-AM83B","PCTP-AM83C","PCTP-AM83D","PCTP-AM84A","PCTP-AM84D","PCTP-TCE2","PCTP-JN06-2","PCTP-JN06-7","PCTP-JN07-3","PCTP-JN07-4","PCTP-JN07-6","PCTP-JN08-2","PCTP-JN08-3","PCTP-JN08-4","PCTP-JN12-6","PCTP-JN15-4","PCTP-JN16-2","PCTP-AM100-3","PCTP-JN17-4","PCTP-JN21-2"]

listingTPU6 = ["RGU8FFsn","eyZUdUdS","dMWrRe9b","aAg5SNeK","2ZgkGh37","Q3e3zr8y","TjFgRzab","vZ4ifHEP","6LkajAyK","T3gMVmR2","jXCpAXsm","utkJB4UA","kPGmUhht","5NWGeHT8","EhsYXNZQ","X3FzPHRm","PCVjrsQL","Fe3K5S3h","mPETjXDE","GiWQQpWs","Xy9VhSLi","DiivqAkj","XUm8hj6Q","h3QAfhPj"]
skuTPU6 = ["PCTP-JN23-1","PCTP-JN23-3","PCTP-JN23-4","PCTP-JN25-2","PCTP-JN33-1","PCTP-JN33-5","PCTP-JN36-5","PCTP-JN37-4","PCTP-JN39-2","PCTP-JN39-3","PCTP-JN39-4","PCTP-JN39-5","PCTP-JN42-1","PCTP-JN42-2","PCTP-JN42-4","PCTP-JN42-7","PCTP-JN45-1","PCTP-JN45-3","PCTP-JN46-1","PCTP-JN46-2","PCTP-JN46-3","PCTP-JN46-4","PCTP-JN47-2","PCTP-CAS02"]

listingTPU7 = ["gZKkppCL","AReMH0VN","uoIhQvo0","TzrA0aQH","rbndSMYu","EVsKfp7o","Wz2s4L9e","wPqvXQ8J"]
skuTPU7 = ["PCTP-AM36K","PCTP-AM10E","PCTP-AM10C","PCTP-AM11E","PCTP-AM11B","PCTP-AM11A","PCTP-AM11C","PCTP-AM11H"]


update_listing(listingTPU7,skuTPU7,phonescase_glossy)


# print("Update Pinkoi Listing? Y or N")
# answer = input()
# if answer == "Y":
#     print("Update start")
#     update_listing(listing_TPU1,SKU_TPU1,phonescase_glossy)
# else:
#     print("Goodbye")
