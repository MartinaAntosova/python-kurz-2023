teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Vypiš seznam průměrných teplot pro každý den.
soucet = 0
for teplota in teploty:
    soucet = soucet + teplota
prumer = soucet / len(teploty)
print(prumer)

# Vypiš seznam ranních teplot.
ranni_teploty = [rano[0] for rano in teploty]
print(ranni_teploty)

# Vypiš seznam nočních teplot.
nocni_teploty = [vecer[2] for vecer in teploty]
print(nocni_teploty)

# Vypiš seznam poledních a nočních teplot.
dvouprvkovy_seznam = [poledne[1] for poledne in teploty], [noc[3] for noc in teploty]
print(dvouprvkovy_seznam)