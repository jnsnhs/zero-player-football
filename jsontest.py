import json


with open("./zerofoot/static/countries/de_1965.json", "r", encoding="utf8") as file:
    j = json.load(file)

print(j["scenario"])
