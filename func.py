def dosomething(foo="Mo Message", bar="More Nothing"):
	thingstring="Hello " + foo + " " + bar
	return(thingstring)

dosomething()

showthing=input("Hey, type something: ")

newstring = dosomething("bah", showthing)
print(newstring)


