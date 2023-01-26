sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadejte kód součástky: ")
pocet_zbozi = int(input("Zadejte počet zboží: "))

if kod_soucastky not in sklad:
    print(f"Součástka s kódem: {kod_soucastky} není na skladě.")
elif pocet_zbozi > sklad[kod_soucastky]:
    print(f"Na skladě NENÍ dostatek zboží, lze prodat jen: {sklad[kod_soucastky]} ks.")
    sklad.pop(kod_soucastky)
#    print(sklad)
else:
    print(f"Na skladě je dostatečné množství součástky s kódem: {kod_soucastky}.")
    sklad[kod_soucastky] = sklad[kod_soucastky] - pocet_zbozi
#    print(sklad)
