data = '''['-1',null,[[['ANDROID_BACKUP',0],['BATTERY_STATS',0],['SMART_SETUP',0],['TRON',0]],-3334737594024971225],[],{'175237375':[10000]}] '''



import json

data = []

with open('data.json', 'r') as f:
    data = json.load(f)


element  = data[2]

print(type(element))