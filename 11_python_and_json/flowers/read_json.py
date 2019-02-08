import json

# read data
with open('data.json', encoding="utf8") as data_file:
    data = json.load(data_file)
    print(data)

# modify data
with open('data.json', 'w', encoding="utf8") as data_file:
    data['nomcommuns']['c'] = "New"

    data['zone'] = {'min':8, 'max':10}


    # json.dump(data, data_file, indent=4, ensure_ascii=False, separators=(',', ': '))
