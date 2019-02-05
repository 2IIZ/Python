import json

json_data = json.dumps(

[
  {
    "nomcommun": "Abélia de Chine",
    "nomcommuns": {
      "a": "Abélia de Chine",
      "b": "Abélie de Chine",
      "c": 0
    },
    "nomlatin": "Abelia chinensis  (R.Br.), synonymes Abelia ascherso...",
    "famille": "Caprifoliaceae",
    "feuillage ": "caduc ou semi-persistant, vert fon...",
    "couleur ": "blanc pur, revers lavé de rose, bout...",
    "hauteur ": "1.5 m.",
    "plantation ": "automne à hiver à printemps.",
    "zone  ": "8 - 10",
  }
]

, indent=4)

with open('data.json', 'w') as outfile:
    json.dump(json_data, outfile, sort_keys=True, indent=4)

print("Writing in file... \n\n"+json_data)
