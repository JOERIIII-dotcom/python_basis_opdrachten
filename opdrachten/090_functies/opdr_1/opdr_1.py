# Opdracht 1 functies
# Naam student:joeri
# Groep:itx3


def write_to_file(bestandsnaam, tekst):
    # Open het bestand in 'append'-modus zodat tekst wordt toegevoegd
    with open(bestandsnaam, 'a') as bestand:
        bestand.write(tekst + '\n')  # Voeg tekst toe met een nieuwe regel

# Voorbeeldgebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "mijn_bestand.txt"
write_to_file(my_file, my_tekst)
