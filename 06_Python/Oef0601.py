# maak een scriopt waarbij gebruik gemaakt wordt van de random library
# print 5 random integers met een waarde tussen 0 en 100
#
# import random
import random

# definieer de functie
def willekeur():
    i = 1 
    while i !=6:
        print(random.randint(0, 10))
        i = i + 1

willekeur()