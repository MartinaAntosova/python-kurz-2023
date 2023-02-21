import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)

slovnik_prospech = {}

bodova_hranice = 60

for key, value in body.items():
    if value >= bodova_hranice:
        print(f"{key}: Pass")
        slovnik_prospech[key] = "Pass"
    else: 
        print(f"{key}: Fail")
        slovnik_prospech[key] = "Fail" 

with open('slovnik_prospech.json', mode='w', encoding='utf-8') as soubor:
    json.dump(slovnik_prospech, soubor)
