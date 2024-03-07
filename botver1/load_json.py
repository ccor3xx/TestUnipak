import json

with open('json1.json') as json1:
    head = json.load(json1)

with open('json2.json') as json2:
    answer = json.load(json2)

with open('json3.json') as json3:
    factor = json.load(json3)

for factors in factor['factor']:
    if factors['id'] == 29:
        spep = factors['name']
    else:
        video = factors['name']