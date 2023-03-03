denne_platby = [
    [134, 240, 13.60],              # pondelok
    [60, 164, 210],                 # utorok
    [65.50, 149, 58, 793],          # streda
    [82, 160],                      # stvrtok
    [59.90, 175, 349, 610, 821],    # piatok
    [139, 241],                     # sobota
    [1675.50, 211, 309]             # nedela
]

# Zjisti celkove naklady (v Kc) za pondeli a uloz vysledek do promenne 'pondelok_naklady'.
pondeli_naklady = []
for hodnoty in denne_platby:
    soucet = sum(hodnoty)
    pondeli_naklady.append(soucet)
print(pondeli_naklady[0])

# Zjisti celkove naklady za kazdy den (v Kc) a uloz vysledek do promenne 'naklady'.
naklady = []
for hodnoty in denne_platby:
    soucet = sum(hodnoty)
    naklady.append(soucet)
print(naklady)

# Spocitej celkove naklady (v Kc) za cely tyden a uloz vysledek do promenne 'celkove_naklady'.
naklady = []
for hodnoty in denne_platby:
    soucet = sum(hodnoty)
    naklady.append(soucet)
    celkove_naklady = sum(naklady)
print(celkove_naklady)