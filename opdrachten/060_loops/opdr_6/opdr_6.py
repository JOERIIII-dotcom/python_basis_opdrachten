# Opdracht 3 input functie
# Naam student:Joeri
# Groep:Itx3

# Hier komt je code...

# Hier start de for-loop

# Gebruik een lijst met pizza's
pizza_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_list.sort()

# Voeg een pizza naar keuze toe
pizza_list.append('yo-favorito')

# Verwijder de pizza die je het minst lekker vindt
pizza_list.remove('olivio')

# Print de eerste 3 pizza's
print(pizza_list[:3])

# Print de middelste pizza
print([pizza_list[len(pizza_list) // 2]])

# Print de laatste 3 pizza's
print(pizza_list[-3:])
