import csv
import sys


def parseheader(firstrow):
# necessary to parse this every time because the number of columns
# varies based on the number of comments, attachem
    fugue_id_num    = firstrow.index("Issue key")
    issue_type_num  = firstrow.index("Issue Type")
    team_num        = firstrow.index("Custom field (Luminal Team)")
    spoints_num     = firstrow.index("Custom field (Story Points)")
    effort_num      = firstrow.index("Custom field (Final Effort Assessment)")

    return fugue_id_num, issue_type_num, team_num, spoints_num, effort_num
#    for n in firstrow:
#        print(n)



samplefile="jirasample.csv"

f = open(samplefile, 'rt')
# try:
reader = csv.reader(f)
rowcount=0
for row in reader:
    thisrow = list(row)
    if rowcount==0:
        headerlist=parseheader(thisrow)
        for headernum in headerlist:
            print(thisrow[headernum]),

    else:
        for n in headerlist:
            print(thisrow[n]),
##        print(fieldname)
##        for headername in headerlist:
##            print(headername),
##    else:
##        print("hi")
##        print(rowcount,": ",thisrow[foodrow])
    rowcount+=1


f.close()
