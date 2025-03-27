# Opdracht 3 Tekst opslaan
# Naam student:Joeri
# Groep:itx3

def encrypt(tekst):
    versleutelde_tekst = ""
    for char in tekst:
        if char.isalpha():
            shift = 5
            start = ord('a') if char.islower() else ord('A')
            versleutelde_tekst += chr(start + (ord(char) - start + shift) % 26)
        else:
            versleutelde_tekst += char
    return versleutelde_tekst

def decrypt(tekst):
    originele_tekst = ""
    for char in tekst:
        if char.isalpha():
            shift = -5
            start = ord('a') if char.islower() else ord('A')
            originele_tekst += chr(start + (ord(char) - start + shift) % 26)
        else:
            originele_tekst += char
    return originele_tekst

tekst = input("Geef de tekst die je wilt encrypten: ")

versleutelde_tekst = encrypt(tekst)
print(f"Geëncrypteerde tekst: {versleutelde_tekst}")

originele_tekst = decrypt(versleutelde_tekst)
print(f"Degeëncrypteerde tekst: {originele_tekst}")



