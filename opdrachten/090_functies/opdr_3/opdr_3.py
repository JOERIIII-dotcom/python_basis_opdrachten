# Opdracht 1 functies
# Naam student:joeri
# Groep:itx3


import math

def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, 'a') as bestand:
        bestand.write(tekst + '\n')

def kilometers_naar_miles(kilometers):
    return kilometers * 0.621371

def miles_naar_kilometers(miles):
    return miles * 1.609344

def kubus_vol(m):
    # je code komt hier
    return m ** 3

def bol_vol(r):
    # je code komt hier
    return (4/3) * math.pi * r**3

zijde = 5
radius = 4

print(kubus_vol(5))
print(bol_vol(4))

kilometers = 1223
miles = 867

miles_omgerekend = kilometers_naar_miles(kilometers)
km_omgerekend = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_omgerekend} miles")
print(f"{miles} miles = {km_omgerekend} kilometers")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "mijn_bestand.txt"
write_to_file(my_file, my_tekst)
