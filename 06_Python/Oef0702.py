# Maak een lijst met 5 getallen (int)
# De uitvoer:
# tel het eerste getal op bij het tweede, tweede bij de derde, etc.
# laatste getal tel je op bij het eerste getal
#
# lijst
mylist = [12, 23, 34, 45, 56]

# loop
for i in range(len(mylist)):
    while i != 4:
        print(mylist[i] + mylist[i+1])
        i = i + 1
    else:
        print(mylist[i] + mylist[0])
        break
