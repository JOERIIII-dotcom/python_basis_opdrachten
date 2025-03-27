

def bereken_btw(bedrag, btw_percentage):
    return bedrag * (btw_percentage / 100)

def verzendkosten(bedrag):
    if bedrag > 100:
        return 0  # Geen verzendkosten als het bedrag groter is dan 100
    else:
        return 5  # Verzendkosten van 5 als het bedrag kleiner is dan 100

def gewicht_toeslag(gewicht):
    if gewicht > 10:
        return 5  # Toeslag van 5 als het gewicht groter is dan 10
    else:
        return 0  # Geen toeslag als het gewicht kleiner of gelijk is aan 10

# Voorbeeld van het berekenen van BTW en verzendkosten
totaalbedrag = 100  # Het bedrag in euro

# Tuple met verschillende gewichten
gewichten = (8, 12, 3, 15, 7)

# Bereken BTW
btw = bereken_btw(totaalbedrag, 21)
print(f"De btw op het bedrag van {totaalbedrag} euro is {btw} euro.")

# Bereken verzendkosten
verzendkosten_bedrag = verzendkosten(totaalbedrag)
print(f"De verzendkosten zijn {verzendkosten_bedrag} euro.")

# Bereken gewichtstoeslag voor elk gewicht in de tuple
for gewicht in gewichten:
    gewichtstoeslag_bedrag = gewicht_toeslag(gewicht)
    print(f"Voor een gewicht van {gewicht} kg is de gewichtstoeslag {gewichtstoeslag_bedrag} euro.")
card.printTotalen(100,50)
# Bereken de totale kosten