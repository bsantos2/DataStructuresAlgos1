"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
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


Call = records()
Call.getAllRecords(calls)

allCalls = {}
x = records()

allNumbers = Call.incomingNumbers + Call.ansNumbers
allNumbers = set(allNumbers)

allCalls = dict.fromkeys(allNumbers)
allCalls = {key: 0 for key in allCalls}

for i in range(0, len(Call.incomingNumbers)):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    allCalls[x.incomingNumber] += x.duration
    allCalls[x.ansNumber] += x.duration

thatTalker = ''
maxDuration = 0
for key in allCalls.keys():
    if allCalls[key] > maxDuration:
        thatTalker = key
        maxDuration = allCalls[key]

print(thatTalker + " spent the longest time, " + str(maxDuration) +
       " seconds, on the phone during September 2016.")

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

Call = records()
Call.getAllRecords(calls)

seenIncomingAnswering = []
durationIncomingAnswering = []
x = records()
'''

myCode = '''for i in range(0, 20):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if x.incomingNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.incomingNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.ansNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.ansNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.incomingNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.incomingNumber)
        durationIncomingAnswering[callIndex] += x.duration
    elif x.ansNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.ansNumbers)
        durationIncomingAnswering[callIndex] += + x.duration
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10000)
#print "20 records take %f" %(timed/10000)

myCode = '''for i in range(0, 40):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if x.incomingNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.incomingNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.ansNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.ansNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.incomingNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.incomingNumber)
        durationIncomingAnswering[callIndex] += x.duration
    elif x.ansNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.ansNumbers)
        durationIncomingAnswering[callIndex] += + x.duration
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10000)
#print "40 records take %f" % (timed/10000)

myCode = '''for i in range(0, 60):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if x.incomingNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.incomingNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.ansNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.ansNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.incomingNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.incomingNumber)
        durationIncomingAnswering[callIndex] += x.duration
    elif x.ansNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.ansNumbers)
        durationIncomingAnswering[callIndex] += + x.duration
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10000)
#print "60 records take %f" %(timed/10000)

myCode = '''for i in range(0, 80):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if x.incomingNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.incomingNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.ansNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.ansNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.incomingNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.incomingNumber)
        durationIncomingAnswering[callIndex] += x.duration
    elif x.ansNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.ansNumbers)
        durationIncomingAnswering[callIndex] += + x.duration
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10000)
#print "80 records take %f" % (timed/10000)


myCode = '''for i in range(0, 100):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if x.incomingNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.incomingNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.ansNumber not in seenIncomingAnswering:
        seenIncomingAnswering.append(x.ansNumber)
        durationIncomingAnswering.append(x.duration)
    elif x.incomingNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.incomingNumber)
        durationIncomingAnswering[callIndex] += x.duration
    elif x.ansNumber in seenIncomingAnswering:
        callIndex = seenIncomingAnswering.index(x.ansNumbers)
        durationIncomingAnswering[callIndex] += + x.duration
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10000)
#print "100 records take %f" %(timed/10000)
