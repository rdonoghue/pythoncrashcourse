list1 = ["ham", "jam", "bread", "cheese"]
list2 = list1
list3 = list1[:]

list1.append("macaroni")
list2.append("chili")
list3.append("quiche")


print("list1: "),
print(list1)
print("list2: "),
print(list2)
print("list3: "),
print(list3)

'''
Ok, so the lesson here is that if I set 1 list directly equal to another list
then it is just a *pointer* to the original list, and if I make changes to 
the initial list, it'll be reflected in the "copied" version (and vice versa).
If I want to ACTUALLY make a copy, I need to use an open slice (thus the :)
and that captures the values rather than the list


Output of this:
list1:  ['ham', 'jam', 'bread', 'cheese', 'macaroni', 'chili']
list2:  ['ham', 'jam', 'bread', 'cheese', 'macaroni', 'chili']
list3:  ['ham', 'jam', 'bread', 'cheese', 'quiche']


'''

#Bonus lesson: Enumerate!
list1 = ["ham", "jam", "bread", "cheese"]
for n,i in enumerate(list1):
#	print(n, i)
	print(n),
	print(":"),
	print(i)