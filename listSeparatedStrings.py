import sys
fileName = sys.argv[1]

lines = [line.strip('\n') for line in open(fileName)]

allStrings = []

import re
separatorRegex = re.compile("[,:]")

for line in lines:
  line = re.sub('[0-9?.~]', '', line)
  stringsInLine = separatorRegex.split(line)
  for string in stringsInLine:
    strippedString = string.strip()
    if len(strippedString) > 0:
      allStrings.append(strippedString)

uniqueStrings = sorted(set(allStrings))

i = 1
for uniqueString in uniqueStrings:
  print(str(i) + '. ' + uniqueString)
  i += 1
