'''
The output should be:
a5|||5|||5|||a5|||5|||5|||a5|||5|||5|||
'''
#foo = ''
#for i in range(3):
#	foo += 'a'
#	for j in range(3):
#		foo += '5'
#	for k in range(3):
#		foo += '|'
#
#print(foo)
#Als volgt aangepast:
foo = ''
for m in range(3):
    for i in range(1):
        foo += 'a'
        for j in range(1):
            foo += '5'
    for l in range(2):
        for k in range(3):
            foo += '|'
        for j in range(1):
            foo += '5'
    for k in range(3):
            foo += '|'

print(foo)