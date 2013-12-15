import sys
fileName = sys.argv[1]

lines = [line.strip('\n') for line in open(fileName)]

allStrings = []

import re
regex = re.compile("[',',':']")

for line in lines:
  stringsInLine = regex.split(line)
  for string in stringsInLine:
    allStrings.append(string.strip())

uniqueStrings = sorted(set(allStrings))

for uniqueString in uniqueStrings:
  print(uniqueString)
