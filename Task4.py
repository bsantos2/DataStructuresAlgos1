"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import timeit

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

class records:
    def __init__(self):
        self.incomingNumber = None
        self.ansNumber = None
        self.time = None
        self.duration = None
        self.incomingNumbers = []
        self.ansNumbers = []
        self.times = []
        self.durations = []

    def getRecord(self, record, index):
        indexedRec = record[index]
        self.incomingNumber = indexedRec[0]
        self.ansNumber = indexedRec[1]
        self.time = indexedRec[2]
        if len(indexedRec) > 3:
            self.duration = int(indexedRec[3])
        else:
            self.duration = 0

    def getAllRecords(self, record):
        i = 0
        self.incomingNumbers = [None] * len(record)
        self.ansNumbers = [None] * len(record)
        self.times = [None] * len(record)
        self.durations= [None] * len(record)
        for x in record:
            self.getRecord(record, i)
            self.incomingNumbers[i] = self.incomingNumber
            self.ansNumbers[i] = self.ansNumber
            self.times[i] = self.time
            self.durations[i] = self.duration
            i += 1

Text = records()
Text.getAllRecords(texts)

Call = records()
Call.getAllRecords(calls)

outgoingCalls = Call.incomingNumbers
textersWhoReceiveCalls = Call.ansNumbers + Text.incomingNumbers + Text.ansNumbers

outgoingCalls = set(outgoingCalls)
textersWhoReceiveCalls = set(textersWhoReceiveCalls)

telemarketers = outgoingCalls.difference(textersWhoReceiveCalls)

print "These numbers could be telemarketers: "

telemarketers = sorted(telemarketers)

for x in telemarketers:
    print(x)

#BEGIN TIMING STUDY
setupCode = '''
from __main__ import records
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
def getAreaCode(number):
    if "(" in number:
        dummy = number.split("(")[1]
        areaCode = dummy.split(")")[0]
    elif " " in number:
        areaCode = number.split(" ")[0]
        areaCode = areaCode[0:4]
    elif number[0:3] == "140":
        areaCode = "140"
    return areaCode

def removeDupes(myList):
    myList = list(dict.fromkeys(myList))
    return myList

Text = records()
Text.getAllRecords(texts)

Call = records()
Call.getAllRecords(calls)

outgoingCalls = Call.incomingNumbers
textersWhoReceiveCalls = Call.ansNumbers + Text.incomingNumbers + Text.ansNumbers

a = outgoingCalls[0:200]
b = outgoingCalls[0:400]
c = outgoingCalls[0:600]
d = outgoingCalls[0:800]
e = outgoingCalls[0:1000]

'''

myCode = '''
removeDupes(outgoingCalls[0:1000])
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode, number = 10000)
#print "1000 records take %f" %(timed/10000)

myCode = '''
removeDupes(outgoingCalls[0:2000])
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode, number = 10000)
#print "2000 records take %f" %(timed/10000)

myCode = '''
removeDupes(outgoingCalls[0:3000])
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode, number = 10000)
#print "3000 records take %f" %(timed/10000)

myCode = '''
removeDupes(outgoingCalls[0:4000])
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode, number = 10000)
#print "4000 records take %f" %(timed/10000)

myCode = '''
removeDupes(outgoingCalls[0:5000])
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode, number = 10000)
#print "5000 records take %f" %(timed/10000)

#BEGIN Analysis on Python sort() plus search telemarketers
myCode1 = '''
telemarketers = []
textersWhoReceiveCalls = []
for x in a:
    if x not in textersWhoReceiveCalls:
        telemarketers.append(x)

telemarketers.sort()
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode1, number = 100)
#print "100 records take %f" %(timed/100)

myCode1 = '''
telemarketers = []
textersWhoReceiveCalls = []
for x in b:
    if x not in textersWhoReceiveCalls:
        telemarketers.append(x)

telemarketers.sort()
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode1, number = 100)
#print "200 records take %f" %(timed/100)

myCode1 = '''
telemarketers = []
textersWhoReceiveCalls = []
for x in c:
    if x not in textersWhoReceiveCalls:
        telemarketers.append(x)

telemarketers.sort()
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode1, number = 100)
#print "300 records take %f" %(timed/100)

myCode1 = '''
telemarketers = []
textersWhoReceiveCalls = []
for x in d:
    if x not in textersWhoReceiveCalls:
        telemarketers.append(x)

telemarketers.sort()
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode1, number = 100)
#print "400 records take %f" %(timed/100)

myCode1 = '''
telemarketers = []
textersWhoReceiveCalls = []
for x in e:
    if x not in textersWhoReceiveCalls:
        telemarketers.append(x)

telemarketers.sort()
'''
timed = timeit.timeit(setup = setupCode, stmt = myCode1, number = 100)
#print "500 records take %f" %(timed/100)