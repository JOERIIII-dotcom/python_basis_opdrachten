# Opdracht 2 tekstbestanden
# Naam student:Joeri
# Groep:ixt3

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

aantal_pogingen = 0

# Print
print(prompt)

# Loop totdat de gebruiker het juiste getal raadt
while True:
    # Gebruiker voert een getal in
    invoer = input("Raad mijn geheime getal: ")

    # Controleer of de invoer een geldig getal is
    try:
        geraden_getal = int(invoer)
    except ValueError:
        print("Voer een geldig getal in.")
        continue

    # Verhoog het aantal pogingen
    aantal_pogingen += 1

    # Vergelijk het geraden getal met het geheime getal
    if geraden_getal < geheim_getal:
        print("Hoger")
    elif geraden_getal > geheim_getal:
        print("Lager")
    else:
        # Als het getal correct is
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break
