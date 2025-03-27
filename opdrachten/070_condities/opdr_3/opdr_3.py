# Opdracht 3 condities
# Naam student:Joeri
# Groep:itx3


# Hier komt je code...
# Normale toegangsprijs
toegangsprijs = 12.50

# Kortingspercentages per leeftijdsgroep
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}

# Leeftijdscategorieën
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de gebruiker om zijn leeftijd
bezoekers_leeftijd = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de categorie en bereken de prijs
for groep, leeftijdsrange in leeftijd.items():
    if leeftijdsrange[0] <= bezoekers_leeftijd <= leeftijdsrange[1]:
        korting = kortings_percentages[groep]
        prijs = toegangsprijs * (1 - korting / 100)
        print(f"U behoort tot de groep {groep}")
        print(f"U krijgt {korting}% korting")
        print(f"U betaalt daarom {prijs:.2f}")
