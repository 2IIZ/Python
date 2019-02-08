import json

with open('data.json', encoding="utf8") as data_file:
    data = json.load(data_file)



    print(json.dumps(data, indent=4, ensure_ascii=False))
