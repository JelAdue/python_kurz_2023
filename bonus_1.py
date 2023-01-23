jmeno_a_prijmeni = input("Zadejte jméno a příjmení: ")
jmeno_a_prijmeni2 = jmeno_a_prijmeni.split(" ")

#aby se osetrilo, co zada uzivatel, nenapsal to dohromady a tak
if len (jmeno_a_prijmeni2) != 2:
    print("Chybný vstup. Zadejte ve formátu JMÉNO PŘÍJMENÍ.")
    exit()

#vsechna velka
print(jmeno_a_prijmeni.upper())

#vsechna mala
print(jmeno_a_prijmeni.lower())

#prvni ve Jmenu a v Prijmeni velke
print(jmeno_a_prijmeni2[0].capitalize() + " " + jmeno_a_prijmeni2[1].capitalize() )

#iniciály
print(jmeno_a_prijmeni2[0][0].upper() + ". " + jmeno_a_prijmeni2[1][0].upper() + ".")

#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
if len(jmeno_a_prijmeni2[0]) >= 5:
    print(jmeno_a_prijmeni2[0][0].upper() + ". " + jmeno_a_prijmeni2[1].capitalize())
else:
    print(jmeno_a_prijmeni2[0].capitalize() + " " + jmeno_a_prijmeni2[1].capitalize())