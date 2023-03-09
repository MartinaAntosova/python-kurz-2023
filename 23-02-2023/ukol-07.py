# Pomocí metody __init__ vytvoř třídu Auto, která bude mít atributy: registrační značka, typ vozidla, najete km, dostupnost).
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne):    
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km 
        self.dostupne = True

    def vypis_informace(self):
        return f"{self.registracni_znacka}, {self.typ_vozidla}, {self.najete_km}, {self.dostupne}"
    
    # Vytvoř metodu pujc_auto. Tato funkce zkontroluje dostupnost vozidla.
    def pujc_auto(self):
        if self.dostupne == True:
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici."
        
    # Vytvoř funkci get_info, která vrátí informaci o vozidle jako řetězec.
    def get_info(self):
        return f"{self.registracni_znacka}, {self.typ_vozidla}"

# Vytvoř objekty se dvěma automobily půjčovny.
cislo1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534", "True")
cislo2 = Auto("1P3 4747", "Škoda Octavia", "41253", "True")

print(cislo1.pujc_auto())
print(cislo2.pujc_auto())
print(cislo1.get_info())
print(cislo2.get_info())

# Zeptej se uživatele, jakou značku si přeje půjčit. 
znacka = input("Jakou značku si přejete půjčit?")

# Pokud uživatel zadá hodnoty "Peugeot" nebo "Škoda", vypiš informace o zvoleném vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().  
def Auto(znacka):
    if znacka == "Peugeot" or "Škoda":
        print(get_info())
    else:
        exit()
