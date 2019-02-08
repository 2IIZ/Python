import json

# load json file
with open('states.json') as file:
    data = json.load(file)

# fo to "states" key and take every data in it.
for state in data['states']:
    # show data keys from "states" key
    print(state['name'], state['abbreviation'])

    # delete key from "states" key
    del state['area_codes']

# generate new json with new data
with open('new_states.json', 'w') as file:
    json.dump(data, file, indent=4)
