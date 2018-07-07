import json
with open("products.json",mode="r") as fp1:

    x=json.load(fp1)
print(list(x['R1'].keys()))