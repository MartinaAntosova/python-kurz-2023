cislo = input("Zadejte prosím telefonní číslo: ")

def telefonni_cislo(cislo):
    if len(cislo) == 9:
        hodnota = True
    elif len(cislo) == 13:
        hodnota = True
    else:
        hodnota = False
    return hodnota
print(telefonni_cislo)

text = input("Zadejte prosím text zprávy: ")

def cena(a, b):
  a = 3
  b = len(text)
  if b < 180:
      cena = a
  elif b > 180:
      cena = 2 * a
  elif b > 360:
      cena = 3 * a 

print(cena)



