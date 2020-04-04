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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def GetLists(calls,texts):
    outgoing = set()
    nonTele = set()
    for item in calls:
        if item[0] not in outgoing:
            outgoing.add(item[0])
        if item[1] not in nonTele:
            nonTele.add(item[1])
    for item in texts:
        if item[0] not in nonTele:
            outgoing.add(item[0])
        if item[1] not in nonTele:
            nonTele.add(item[1]) 
    return outgoing,nonTele
    
def IdentifyTeleMarketNos(outgoingCalls,nonTele):
    Lists = set()
    for item in outgoingCalls:
        #print(item[2][3:10])
        if item not in nonTele:
            Lists.add(item)
    return Lists
outgoingCalls,nonTele = GetLists(calls,texts)
teleMArketingNumbers = IdentifyTeleMarketNos(outgoingCalls,nonTele)
print("These numbers could be telemarketers: ")
for i in sorted(teleMArketingNumbers):
    print(i)
