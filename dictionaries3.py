# lists in a dictionary
clothes1= {
	'shirt' : 'blue', 
	'pants' : 'red', 	
	'hat' : ['yellow', 'black']
	}


for x,y in clothes1.items():
	print(x.title() + ":")
#	print(len(y)),
#	print(y)
	isstring=isinstance(y,basestring)
	if isstring:
		print("\t" + y.title())
	else:
		for z in y:
			print("\t" + z.title())
	
# I am >< to installing python 3 to see if this is one of those cases
# Ok, fuck it, installing Python 3 to see if this runs differently

# NO IT STILL FUCKING DOES THIS THING

# GOD DAMMIT YOU CHEATING SON OF A BITCH
# Ok, Added the fucking isintance check after digging around stackoverflow 
# because the example in the book is a CHEATING ASS PIECE OF SHIT
# and it only works in python2 because basestring apparently doesn't
# exist in Python3 because FUCK YOU THAT'S WHY


# I could put a dictionary in a dictionary now, but honest to god I think
# I'm just too pissed to even try. 