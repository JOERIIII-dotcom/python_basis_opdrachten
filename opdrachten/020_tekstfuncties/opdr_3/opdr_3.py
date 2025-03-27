# Opdracht 3 tekstfuncties
# Naam student:joeri
# Groep:itx3

# Hier komt je code...


tree = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    "   ***   ",
    "   ***   ",
    "   ***   "
]

# Aantal bomen
num_trees = 10

# Loop door elke rij van de boom
for row in tree:
    # Print de rij van elke boom naast elkaar
    print(row * num_trees)