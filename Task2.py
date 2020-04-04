"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def GetRecordsbyDate(calls):
    Lists = {}
    for item in calls:
        #print(item[2][3:10])
        if item[2][3:10] == '09-2016':
            if item[0] not in Lists:
                Lists[item[0]] = int(item[3])
            else:
                Lists[item[0]] += int(item[3])
            if item[1] not in Lists:
                Lists[item[1]] = int(item[3])
            else:
                Lists[item[1]] += int(item[3])
        
    return Lists
phoneNumbers = GetRecordsbyDate(calls)
max_key = max(phoneNumbers, key=phoneNumbers.get)
#print(max_value,max_key)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key,phoneNumbers[max_key]))
