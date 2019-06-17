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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
class records:
    def __init__(self):
        self.incomingNumber = None
        self.ansNumber = None
        self.time = None
        self.duration = None

    def getRecord(self, record, index):
        indexedRec = record[index]
        self.incomingNumber = indexedRec[0]
        self.ansNumber = indexedRec[1]
        self.time = indexedRec[2]
        if len(indexedRec) > 3:
            self.duration = indexedRec[3]
        else:
            self.duration = None

firstText = records()
firstText.getRecord(texts, 0)
print("First record of texts, " + firstText.incomingNumber +
      " texts " + firstText.ansNumber + " at time " + firstText.time)

lastCall = records()
lastCall.getRecord(calls, len(calls) - 1)
print("Last record of calls, " + lastCall.incomingNumber +
      " calls " + lastCall.ansNumber + " at time " + lastCall.time +
      " lasting " + lastCall.duration + " seconds")

#BEGIN TIMING STUDY
''''''
setupCode = '''
from __main__ import records
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
'''

#BEGIN TIMING STUDY
myCode = '''
lastCall = records()
lastCall.getRecord(calls, len(calls) - 1)'''
timed = timeit.timeit(setup = setupCode,
            stmt = myCode,
            number = 100)
#print "Single Loop Call %f" % (timed/100)