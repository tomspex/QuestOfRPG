import json

file = open("items.json")
items = json.load(file)
file.close()

file = open("locations.json")
locations = json.load(file)
file.close()
