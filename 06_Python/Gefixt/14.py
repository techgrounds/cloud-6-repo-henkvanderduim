'''
The output should be:
True
'''
def rtn(x):
	return(x)

foo = rtn(3)
# < i.p.v. > en het werkt
#if foo > rtn(4):
if foo < rtn(4):
	print(True)
else:
	print(False)