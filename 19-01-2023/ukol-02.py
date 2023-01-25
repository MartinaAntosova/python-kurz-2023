sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

# Vypiš "Zadejte kód součástky: "
kod_soucastky = input("Zadejte kód součástky: ")

# Jestliže je součástka se zadaným kódem na skladě, vypiš "Zadejte množství: "
if kod_soucastky in sklad:
    mnozstvi = int(input("Zadejte množství: "))

    # Jestliže je množství na skladě menší než zadané množství, vypiš, že lze prodat pouze omezené množství kusů a odeber součástku ze slovníku. Poté vypiš stav skladu.
    if int(sklad[kod_soucastky]) < mnozstvi: 
      print(f'Bohužel součástky s kódem {kod_soucastky} je na skladě pouze {sklad[kod_soucastky]} ks.')
      sklad.pop(kod_soucastky)
      print(sklad)

    # Jestliže je množství na skladě větší než zadané množství, vypiš, že lze poptávku uspokojit v plné výši a sniž počet součástek na skladě o zadané množství. Poté vypiš stav skladu.
    if int(sklad[kod_soucastky]) > mnozstvi:
      print(f'Součástky s kódem {kod_soucastky} je na skladě až {sklad[kod_soucastky]} ks. Poptávku lze tedy uspokojit v plné výši.')
      sklad[kod_soucastky] = sklad[kod_soucastky] - mnozstvi
      print(sklad)

# Jestliže není součástka se zadaným kódem na skladě, vypiš zprávu, že součástka není skladem.
else: 
    print(f'Bohužel součástku s kódem {kod_soucastky} nemáme skladem.')
