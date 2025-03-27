# Opdracht 4 condities
# Naam student:Joeri
# Groep:itx3


# Toppingslijst
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van beschikbare toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Input voor keuze
topping_keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze geldig is
topping_gevonden = False
for topping, prijs in toppings:
    if topping_keuze == topping:
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        topping_gevonden = True
        break

if not topping_gevonden:
    print("Uw keuze zit niet in ons assortiment")