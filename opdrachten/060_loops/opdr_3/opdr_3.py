# Opdracht 3 input functie
# Naam student:joeri
# Groep:itx3

# Hier komt je code...

# Hier start de for-loop




# Maak een lege lijst
my_list = []

# Gebruik een for-loop en range-functie om de getallen toe te voegen
for i in range(3, 81, 3):  # Start bij 3, eindig bij 81 (exclusief), stapgrootte van 3
    resultaat = (i ** 2) / 3  # Getal in het kwadraat en gedeeld door 3
    my_list.append(resultaat)

# Print de lijst
print(my_list)
