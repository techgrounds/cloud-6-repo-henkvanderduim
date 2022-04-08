# Data Types en Comments
Een computer werkt met binaire code. Om te zien of een binaire code een getal of een letter is, zal het data type goed gedefinieerd moeten worden.  

## Data Typen
- Boolean: True of False
- String: Karakters, weergegeven tussen "" en ''
- Int: Integer oftewel een geheel getal. Kan zowel positief als negatief zijn
- Float: Een decimaal getal
- Comments: Dit wordt niet gezien als code. Dit kun je gebruiken om een korte beschrijving te geven van wat een stuk code doet. Ook kun je code op die manier 'uitzetten'.

## Oefening 1
### Code
```python
# variabele a
a = 'int'

# variabele b
b = 7

# variabele c
c = False

# variabele d
d = "18.5"

# M.b.v. het commando 'type' achterhalen welk data type erin de variabelen zit.
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# nieuwe variabele opvoeren die een foutmelding geeft
#x = b + d

# variabele x aanpassen zodat het werkt
x = b + float(d)
print(x)
```
### Resultaat
#### Data Types achterhalen
![result](../00_includes/Oef0301-result1.png)

#### Nieuw variabele met foutmelding
![result](../00_includes/Oef0301-result2.png)

#### Nu met de juiste syntax
![result](../00_includes/Oef0301-result3.png)

## Oefening 2
De input() functie geeft altijd een 'str' klasse aan als data type. Als je dit anders wil, dan zul je bij het input() commando moeten aangeven wat je verwacht.  
- int(input("waarde: "))
- float(input("waarde: "))

### Code
```python
# Spelen met de input() functie en variabelen
# input opvragen
waarde = input("geef een waarde: ")

# welk data type is ingevoerd?
print(type(waarde))
```
### Resultaat
![result](../00_includes/Oef0302-result.png)