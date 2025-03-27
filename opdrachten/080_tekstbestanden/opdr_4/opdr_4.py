# Opdracht 4 Tekst opslaan
# Naam student: Joeri
# Groep:itx3


# Party enquete


# Lijst van vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Openen van het tekstbestand voor het opslaan van de antwoorden
with open('feestganger_gegevens.txt', 'a') as bestand:
    while True:
       
        feestganger = {}
        
        # Vragen stellen aan de feestganger en antwoorden opslaan in de dictionary
        for i, vraag in enumerate(vragen, 1):
            antwoord = input(f"{i}. {vraag} ")
            if i == 1:
                feestganger["voornaam"] = antwoord
            elif i == 2:
                feestganger["achternaam"] = antwoord
            elif i == 3:
                feestganger["drank"] = antwoord
            elif i == 4:
                feestganger["eten"] = antwoord
        
        # Gegevens naar het tekstbestand schrijven
        bestand.write(f"----\n")
        for key, value in feestganger.items():
            bestand.write(f"{key}: {value}\n")
        
        # Bedankt-bericht voor de feestganger
        print("\nBedankt voor het invullen!")
        print("See you at the party.\n")
        print("lelijkerd.\n")
        
        # Vraag of er nog een feestganger is
        nog_meer = input("Wil je nog een feestganger toevoegen? (ja/nee): ")
        if nog_meer.lower() != 'ja':
            break
