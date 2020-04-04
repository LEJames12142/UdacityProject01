"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

uniqueLists = {}
def Unique(listText):
    for i in listText:
        if i[0] not in uniqueLists:
            #uniqueLists.append(i[0])
            uniqueLists[i[0]] = i[2]
        if i[1] not in uniqueLists:
            uniqueLists[i[1]] = i[2]
    return uniqueLists
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueLists = Unique(texts)
uniqueLists = Unique(calls)
print("There are {} different telephone numbers in the records.".format(len(uniqueLists)))
#print(len(Unique(calls)))
#print(len(Unique(texts)))
#print(Unique(calls))
