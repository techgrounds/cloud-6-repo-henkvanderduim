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