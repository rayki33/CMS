import pandas as pd

def read_csvfile(datafile):
    data = pd.read_csv(datafile)
    datasets = data.to_numpy()
    return datasets

adImages = read_csvfile('data/ame_addionalImages.csv')

# print(adImages)
# print(adImages[0,0])

imageSet = []
productID = []

i = 0
while i < len(adImages):
    if imageSet[0, 1] == adImages[0, i]:
        imageSet.append(adImages[0, i])

    i = i+1

print(imageSet)

# for item in adImages:
#     # print(item)
#
#     print(item[0])
#     if imageSet[0] == item[0]:
#         imageSet.append(item[0])
