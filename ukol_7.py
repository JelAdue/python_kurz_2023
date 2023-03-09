class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla"
        else:
            return f"Vozidlo není k dispozici"
    
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka} Značka a typ vozidla: {self.typ_vozidla}."

skoda = Auto("1P3 4747", "Škoda Octavia", "41253")
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")

vypujceni = input("Jakou značku si chcete půjčit? ")

if vypujceni == "Škoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
    #print(skoda.pujc_auto()) #Otestuj, že program nedovolí půjčit stejné auto dvakrát.
elif vypujceni == "Peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
else:
    print("Tuto značku nemáme v nabídce.")
