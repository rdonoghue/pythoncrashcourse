import csv
import sys



def parseheader(firstrow):
#    foodval = firstrow.index("Food")
#    print("Food is value ",foodval)
#    return foodval
    for n in firstrow:
        print(n)


samplefile="jirasample.csv"

f = open(samplefile, 'rt')
# try:
reader = csv.reader(f)
rowcount=0
for row in reader:
    thisrow = list(row)
    if rowcount==0:
        foodrow=parseheader(thisrow)
##    else:
##        print(fieldname)
    else:
        break
    rowcount+=1
#    print(row)

# finally:
f.close()
