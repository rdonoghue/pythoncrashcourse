foo = "Hello World Three"
print(foo)

# Oooh, methods, specifically for title case, all upper & all lower
print("Title:\t\t"),
print(foo.title())

print("Upper:\t\t"),
print(foo.upper())

print("Lower:\t\t"),
print(foo.lower())

#a pparently this just works to right & left (and can be rstrip
# or lstrip, as appropriate)
print("Stripped:\t"),
print(foo.strip())


foolist = ["green", "red", "blue"]
# Oy. Accidentally created a tuple by using () rather than [] so that was a 
# quick education in immutabilty when I tried to 

print(foolist[0].title())

# position -1 == last position! Handy!
# ooh, in fact nagative values count forom the end, so -2 is red!


print(foolist[-2].title())

print(foolist)
foolist[0] = "purple"
print(foolist)
foolist.append('yellow')
print(foolist)
foolist.insert(2,'orange')
print(foolist)
del foolist[3]
print(foolist)
tempvalue =foolist.pop(3)
print(tempvalue)
print(foolist)
foolist.append('red')
print(foolist)
foolist.remove('red')
# ^^^ Only removed the first instance.  Curious.
print(foolist)