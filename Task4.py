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
def GetLists(lists):
    outgoing = []
    incoming = []
    for item in lists:
        if item[0] not in outgoing:
            outgoing.append(item[0])
        if item[1] not in incoming:
            incoming.append(item[1])
    return outgoing,incoming
    
def IdentifyTeleMarketNos(outgoingCalls,AllNos):
    Lists = []
    for item in outgoingCalls:
        #print(item[2][3:10])
        if item not in AllNos:
            Lists.append(item)
    return Lists
outgoingCalls,incomingCalls = GetLists(calls)
outgoingTexts,incomingTexts = GetLists(texts)
AllOtherNos = incomingCalls + outgoingTexts + incomingTexts
teleMArketingNumbers = IdentifyTeleMarketNos(outgoingCalls,AllOtherNos)
print("These numbers could be telemarketers: ")
for i in sorted(teleMArketingNumbers):
    print(i)
