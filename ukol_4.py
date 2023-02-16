import math

def overeni_cisla(tel_cislo:str):
    """Funkce na ověření platnosti zadaného čísla.
    Platné číslo = len 9 or len = 13 a předvolba je +420.
    Funkce smaže mezery v zadaném čísle"""
    cislo = tel_cislo.replace(" ","")
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo[0:4] == "+420":
        return True
    else:
        return False

def cena_zpravy(zprava:str, cena:int = 3):
    """Funkce spočte cenu zprávy.
    Uživatel platí 3 Kč za každých započatých 180 znaků."""
    delka = math.ceil(len(zprava)/180)
    return delka * cena

cislo_uzivatel = input("Zadejte své telefoní číslo:")

if overeni_cisla(cislo_uzivatel) == True:
    zprava_uzivatel = input("Zadejte zprávu:")
    print(f"Cena zprávy je: {cena_zpravy(zprava_uzivatel)} Kč.")
else:
    print("Zadané číslo je neplatné.")
