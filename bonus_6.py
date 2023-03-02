import re

re_jmeno = re.compile(r"\w{6,10}")
re_email = re.compile(r"^[a-zA-Z\d\_\-\+\"\=]{1,}[a-zA-Z\_\d\-\.\+\"\=][a-zA-Z\d\_\-\+\"\=]{1,}@[a-zA-Z\[\]][a-zA-Z\[\]\-]{1,}\.?[a-zA-Z\-\[\]]{1,}\.?[a-zA-Z\-\[\]]{1,}\.[a-zA-Z\-\[\]]{1,}$|^[a-zA-Z\d\_\-\+\"\=]{1,}[a-zA-Z\_\d\-\.\+\"\=][a-zA-Z\d\_\-\+\"\=]{1,}@\[?[\d\[\]\-]{1,3}\.?[\d\-\[\]]{1,3}\.?[\d\-\[\]]{1,3}\.[\d\-\[\]]{1,3}\]?$")

#takhle to funguje i na tu posledni, co mi tam zustala, ale prijde mi to takove skarede...
#re_email = re.compile(r"^[a-zA-Z\d\_\-\+\"\=]{1,}[a-zA-Z\_\d\-\.\+\"\=][a-zA-Z\d\_\-\+\"\=]{1,}@[a-zA-Z\[\]][a-zA-Z\[\]\-]{1,}\.?[a-zA-Z\-\[\]]{1,}\.?[a-zA-Z\-\[\]]{1,}\.[a-vA-V\-\[\]]{1,}$|^[a-zA-Z\d\_\-\+\"\=]{1,}[a-zA-Z\_\d\-\.\+\"\=][a-zA-Z\d\_\-\+\"\=]{1,}@\[?[\d\[\]\-]{1,3}\.?[\d\-\[\]]{1,3}\.?[\d\-\[\]]{1,3}\.[\d\-\[\]]{1,3}\]?$")

re_heslo = re.compile(r"^[\w\_\-\.\+\=]{12,30}$")

jmeno = input("Zadejte přihlašovací jméno: ")
email = input("Zadejte e-mailovou adresu: ")
heslo = input("Zadejte heslo: ")

jmeno_ok = re_jmeno.fullmatch(jmeno)
email_ok = re_email.fullmatch(email)
heslo_ok = re_heslo.fullmatch(heslo)

if jmeno_ok:
    print("Zadané uživatelské jméno je v pořádku.")
else:
    print("Špatný formát zadaného uživatelského jména.")

if email_ok:
    print("Zadaná e-mailová adresa je v pořádku.")
else:
    print("Špatný formát zadané e-mailové adresy.")

if heslo_ok:
    print("Zadané heslo je v pořádku.")
else:
    print("Špatný formát zadaného hesla.")