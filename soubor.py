import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)

bodova_hranice = 60

for key, value in body.items():
    if value >= bodova_hranice:
        print(f"{key}: Pass")
    else: 
        print(f"{key}: Fail") 

with open('prospech.json', mode='w', encoding='utf-8') as soubor:
    json.dump(body, soubor)
