# Opdracht 1 input function
# Naam student:joeri
# Groep:itx3

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

zijde_1 = float(input("Geef de lengte van de eerste zijde\n"))
zijde_2 = float(input("Geef de lengte van de tweede zijde\n"))



hypotenusa = math.sqrt(zijde_1**2 + zijde_2**2)

print(f"De lengte van de schuine zijde is: {hypotenusa}")

#deze was wel pittig