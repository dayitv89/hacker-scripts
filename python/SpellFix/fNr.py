import sys
from spellCheck import *

val = ''
lineNo = 0
print("\n\n=============================================================\n")
print(sys.argv[1])
print("\n--------------------------------------------------------------\n")
for line in open(sys.argv[1], 'r'):
    lineNo += 1
    lines = re.findall('[a-z]+', line.lower())
    for word in lines:
        a = correct(word.lower())
        if a != word.lower():
            val = 'Line: ' + str(lineNo) + ' => ' + word + ' != ' + a + '\n'
            print val
print("\n\n--------------------------------------------------------------\n\n")
