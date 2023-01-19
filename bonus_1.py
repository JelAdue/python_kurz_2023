jmeno = input("Zadejte jméno:")
prijmeni = input ("Zadejte příjmení:")

jmeno_a_prijmeni = jmeno + " " + prijmeni

#vsechna velka
print(jmeno_a_prijmeni.upper())

#vsechna mala
print(jmeno_a_prijmeni.lower())

#prvni ve Jmenu a v Prijmeni velke
print(jmeno.capitalize() + " " + prijmeni.capitalize())

#iniciály
print(jmeno[0].upper() + ". " + prijmeni[0].upper() + ".")


#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)

if len(jmeno) >= 5:
    print(jmeno[0].upper() + ". " + prijmeni.capitalize())
else:
    print(jmeno.capitalize() + " " + prijmeni.capitalize())
