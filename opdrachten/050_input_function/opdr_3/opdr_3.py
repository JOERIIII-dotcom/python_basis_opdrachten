# Opdracht 3 input functie
# Naam student:joeri
# Groep:itx3



# Stap 1: Vraag de gebruiker om minimaal 5 objecten in te voeren, gescheiden door komma's
input_str = input("Voer minimaal 5 objecten in, gescheiden door komma's: ")

# Stap 2: Splits de invoer op komma's om een lijst van objecten te maken
input_lijst = input_str.split(", ")

# Stap 3: Controleer of er minimaal 5 objecten zijn ingevoerd
if len(input_lijst) < 5:
    print("Je hebt minder dan 5 objecten ingevoerd. Probeer het opnieuw.")
else:
    # Stap 4: Maak een nieuwe lijst met de objecten in omgekeerde volgorde
    omgekeerde_lijst = []
    for item in input_lijst:
        omgekeerde_lijst.append(item)

    # Stap 5: Sorteer de omgekeerde lijst
    omgekeerde_lijst.sort(reverse=True)
    #print
    print("Gesorteerde lijst in omgekeerde volgorde:", omgekeerde_lijst)
