# Opdracht 2 lists
# Naam student:joeri
# Groep:itx3


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

for rivier, landen in rivier_info.items():
    print(f"De {rivier} stroomt door de landen: {', '.join(landen)}")