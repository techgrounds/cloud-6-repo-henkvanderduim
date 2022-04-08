# vraag om een getal. 
# geef een reactie op basis van het volgende:
# - hoger dan 100 
# - lager dan 100
# - gelijk aan 100 en zo ja stop de loop
#
# Variabele getal
getal = int(input("Geef een willekeurig getal: "))
while getal != 100:
    if getal > 100:
        print(getal, "dit is hoger dan 100")
        getal = int(input("Geef een willekeurig getal: "))
    elif getal < 100:
        print(getal, "dit is lager aan 100")
        getal = int(input("Geef een willekeurig getal: "))
else:
    if getal == 100:
        print(getal, "dit is gelijk aan 100")