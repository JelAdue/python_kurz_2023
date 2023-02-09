import json

with open("body.json", encoding="utf=8") as soubor:
    body = json.load(soubor)

prospech = {}
for kdo,bodovy_zisk in body.items():
    if bodovy_zisk >= 60:
        bodovy_zisk = "Pass"
    else:
        bodovy_zisk = "Fail"
    prospech[kdo] = bodovy_zisk 

print(prospech)

with open('prospech.json', mode='w', encoding='utf-8') as novy_soubor:
    json.dump(prospech, novy_soubor)