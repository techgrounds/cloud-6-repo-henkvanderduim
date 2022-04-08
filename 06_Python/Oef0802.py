# maak een script waarbij input gevraagd wordt:
# - voornaam
# - achternaam
# - beroep
# - bedrijf
# Sla het op in dictionary
# Schrijf de informatie naar een CSV bestand
# Het CSV bestand mag niet overschreven worden als
# er informatie wordt toegevoegd
#
# import csv
import csv

# paadje aanleggen
new_path = open("test.csv", "w")

# maak dictionary
mydict = {
    "Voornaam": "",
    "Achternaam": "",
    "Beroep": "",
    "Bedrijf": ""
}

# loop
while True:
    # Vraag input
    n = input("Wat is je voornaam? ")
    a = input("Wat is je achternaam? ")
    b = input("Wat is je beroep? ")
    c = input("Hoe heet je bedrijf? ")

    # voeg toe aan dictionary
    mydict.update({"Voornaam": n})
    mydict.update({"Achternaam": a})
    mydict.update({"Beroep": b})
    mydict.update({"Bedrijf": c})

    # stoppen ja of nee
    cont = input("Meer collega's invoeren (Y/N)? ")

    # stoppen met de handel
    if cont == "N":
        break

# naar CSV schrijven
z = csv.writer(new_path)
for new_k, new_v in mydict.items():
    z.writerow([new_k, new_v])

new_path.close()