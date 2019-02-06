import json

json_data = {
    "nomcommun": "Abélia de Chine",
    "nomcommuns": {
      "a": "Abélia de Chine",
      "b": "Abélie de Chine",
      "c": 0
    },
    "nomlatin": "Abelia chinensis  (R.Br.), synonymes Abelia ascherso...",
    "famille": "Caprifoliaceae",
    "feuillage": "caduc ou semi-persistant, vert fon...",
    "couleur": "blanc pur, revers lavé de rose, bout...",
    "hauteur": "1.5 m.",
    "plantation": "automne à hiver à printemps.",
    "zone": "8 - 10",
}

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_data, outfile, indent=4, ensure_ascii=False)

print("Writing in file... \n\n"+json.dumps(json_data, indent=4, ensure_ascii=False))
