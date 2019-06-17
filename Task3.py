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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
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


Call = records()
Call.getAllRecords(calls)

areaCodes = []

i = 0
x = records()
counter = 0
counterBangalore = 0

for i in range(0, len(Call.incomingNumbers)):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1

percentage = 100 * float(counter) / float(counterBangalore)

print("The numbers called by people in Bangalore have codes:")
areaCodes = sorted(areaCodes)
for x in areaCodes:
    print(x)

print("{:.2f}".format(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

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

Call = records()
Call.getAllRecords(calls)

areaCodes = []

i = 0
x = records()
counter = 0
counterBangalore = 0
'''

myCode = '''
for i in range(0, 20):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 100000)
#print "20 records take %f" %(timed/100000)

myCode = '''
for i in range(0, 40):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 100000)
#print "40 records take %f" %(timed/100000)

myCode = '''
for i in range(0, 60):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 100000)
#print "60 records take %f" %(timed/100000)

myCode = '''
for i in range(0, 80):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 100000)
#print "80 records take %f" %(timed/100000)


myCode = '''
for i in range(0, 100):
    x.incomingNumber = Call.incomingNumbers[i]
    x.ansNumber = Call.ansNumbers[i]
    x.duration = Call.durations[i]
    if "(080)" in x.incomingNumber:
        counterBangalore += 1
        dummy = getAreaCode(x.ansNumber)
        if dummy not in areaCodes:
            areaCodes.append(dummy)
        if dummy == "080":
            counter += 1
'''
timed = timeit.timeit(setup = setupCode,
                      stmt = myCode,
                      number = 100000)
#print "100 records take %f" %(timed/100000)
