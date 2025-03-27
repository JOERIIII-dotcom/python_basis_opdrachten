# Opdracht 1 while-loops
# Naam student:Joeri    
# Groep:itx3

# Jouw code komt hier

# Enquêtevragen
enquete_vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Antwoorden verzamelen
antwoorden = []
for vraag in enquete_vragen:
    antwoord = input(vraag + "\n")
    antwoorden.append(antwoord)

# Resultaten opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    for vraag, antwoord in zip(enquete_vragen, antwoorden):
        bestand.write(f"{vraag}: {antwoord}\n")

print("De antwoorden zijn opgeslagen in 'enquete_resultaten.txt'")