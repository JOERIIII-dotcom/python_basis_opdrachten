# Opdracht 1 functies
# Naam student:joeri
# Groep:ixt3


def write_to_file(bestandsnaam, tekst):
    # Open het bestand in 'append'-modus zodat tekst wordt toegevoegd
    with open(bestandsnaam, 'a') as bestand:
        bestand.write(tekst + '\n')  # Voeg tekst toe met een nieuwe regel

def kilometers_naar_miles(kilometers):
    return kilometers * 0.621371

def miles_naar_kilometers(miles):
    return miles * 1.609344

# Voorbeeldgebruik van de functies
kilometers = 1223
miles = 867

miles_omgerekend = kilometers_naar_miles(kilometers)
km_omgerekend = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_omgerekend} miles")
print(f"{miles} miles = {km_omgerekend} kilometers")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "mijn_bestand.txt"
write_to_file(my_file, my_tekst)