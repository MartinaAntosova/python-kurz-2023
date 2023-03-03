cislo = input("Zadejte prosím telefonní číslo: ")

def telefonni_cislo(cislo):
    if len(cislo) == 9:
        hodnota = True
        print(input("Zadejte prosím text zprávy: "))
    elif len(cislo) == 13 and cislo == str(+420):
        hodnota = True
        print(input("Zadejte prosím text zprávy: "))
    else:
        hodnota = False
        print("Vložili jste špatný tvar čísla.")
    return hodnota

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



