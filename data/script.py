data = '''['-1',null,[[['ANDROID_BACKUP',0],['BATTERY_STATS',0],['SMART_SETUP',0],['TRON',0]],-3334737594024971225],[],{'175237375':[10000]}] '''

python_data = ['-1', None,
               [[['ANDROID_BACKUP', 0], ['BATTERY_STATS', 0], ['SMART_SETUP', 0], ['TRON', 0]], -3334737594024971225],
               [], {'175237375': [10000]}]

import json

with open('data.json', 'w') as f:
    json.dump(python_data, f)
