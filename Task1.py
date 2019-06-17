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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
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
            self.duration = indexedRec[3]
        else:
            self.duration = None

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

allNumbers = Text.incomingNumbers + Text.ansNumbers + Call.incomingNumbers + Call.ansNumbers

allNumbers = set(allNumbers)

print("There are " + str(len(allNumbers)) + " different telephone numbers in the records.")

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
Text = records()

a = calls[0:100]
b = calls[0:200]
c = calls[0:300]
d = calls[0:400]
e = calls[0:500]
'''

myCode = '''
Call.getAllRecords(a)
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10)
#print "100 records take %f" %(timed/10)

myCode = '''
Call.getAllRecords(b)
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10)
#print "200 records take %f" %(timed/10)

myCode = '''
Call.getAllRecords(c)
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10)
#print "300 records take %f" %(timed/10)

myCode = '''
Call.getAllRecords(d)
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10)
#print "400 records take %f" %(timed/10)

myCode = '''
Call.getAllRecords(e)
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 10)
#print "500 records take %f" %(timed/10)


