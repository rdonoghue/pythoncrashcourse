clothes0= {
	'shirt' : 'lavender', 
	'pants' : 'blue', 	
	'hat' : 'blue'
	}

clothes1= {
	'shirt' : 'blue', 
	'pants' : 'red', 	
	'hat' : 'yellow'
	}
clothes2= {
	'shirt' : 'turquoise', 
	'pants' : 'green', 	
	'hat' : 'black'
	}

allclothes = [clothes0, clothes1, clothes2]

for aparrel in allclothes:
	print aparrel


'''

Ok, hiding all this while I mess with the next bit

clothes1['socks'] = 'purple'

print(clothes1)
print
print(clothes1['socks'])
print
clothes1['socks'] = 'orange'
print(clothes1['socks'])
print
del clothes1['socks']
print(clothes1)

for x,y in clothes1.items():
	print(x),
	print("\t:"),
	print(y)
# ^^^ that items() seems to be the key. Just doing clothes1 throws an error

print
# keys() will get just keys
for x in clothes1.keys():
	print(x)
print
# Huh. Apparently keys() is the default pehavior
for x in clothes1:
	print(x)
print

# Alternately, we hit values()
for x in clothes1.values():
	print(x)
print

# We an also pre-sort
for x in sorted(clothes1.keys()):
	print(x)
print
'''
