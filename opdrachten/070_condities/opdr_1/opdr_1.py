# Opdracht 1 condities
# Naam student:Joeri
# Groep:itx3

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

# Maak een lijst met de getallen van 1 t/m 10
getallen_lijst = [i for i in range(1, 11)]

# Print alleen de getallen groter dan 4
for getal in getallen_lijst:
    if getal > 4:
        print(getal, end=', ')