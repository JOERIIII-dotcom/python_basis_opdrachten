# Opdracht 2 berekeningen
# Naam student:joeri
# Groep:itx3

# Hier komt je code...

gastenlijst = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Print de initiële lijst
print("Eerste gastenlijst:", gastenlijst)

# Verwijder Marie uit de lijst
gastenlijst.remove("Marie")

# Print de lijst na het verwijderen van Marie
print("Lijst na Marie's afmelding:", gastenlijst)

# Voeg George toe naast Kees
kees_index = gastenlijst.index("Kees")  # Zoek de index van Kees
gastenlijst.insert(kees_index + 1, "George")  # Voeg George toe na Kees

# Print de lijst na het toevoegen van George
print("Lijst na het toevoegen van George:", gastenlijst)