# Opdracht 1 functies
# Naam student: joeri
# Groep:itx3


def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        if persoon['tussenvoegsel']:
            naam = f"{persoon['voornaam']} {persoon['tussenvoegsel']} {persoon['achternaam']}"
        else:
            naam = f"{persoon['voornaam']} {persoon['achternaam']}"
        print(naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
