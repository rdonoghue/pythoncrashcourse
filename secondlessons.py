foolist = ["green", "red", "blue"]
foolist.sort()
#^^^^ Permanent 
print(foolist)

foolist.sort(reverse = True)
print(foolist)

print(sorted(foolist))
# ^^^ Temporary
print(foolist)

newlist = ["ham", "jam", "bread", "cheese"]
newlist.reverse()
#^^^ Also Permanent
print(newlist)
print(len(newlist))

for food in newlist:
	print(food)

for number in range(1,5):
	print(number)

numlist = list(range(1,6))
# ^^^ list function! Handy!

print(numlist)
# Apparently if a list is all numbers, I can do tricks:
print min(numlist)
print max(numlist)
print sum(numlist)
# ^^^ Remember sum when I get back to the 7th Sea math

# One line list building
squares = [value**2 for value in range(1,11)]
print(squares)
# Apparently this is called a "List Comprehension"
# Advanced technique. Really weird order of operations from my perspective.
# The fact that that the value can proceed the for is a little brain bending
# But there's no colon, so maybe the thinking looks different.

# Slices
print(squares[2:6])
print(squares[3:])
print(squares[:6])
print(squares[:])
