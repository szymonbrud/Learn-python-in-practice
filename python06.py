trainText = input()

tableOfTextFromBeginning = []
tableOfTextFromEnd = []

isTheSameLetter = True

for fromBeginning in trainText:
    tableOfTextFromBeginning.append(fromBeginning)

for fromEnd in range(len(trainText) -1, -1, -1):
    tableOfTextFromEnd.append(trainText[fromEnd])


for index in range(len(trainText)):
    if(tableOfTextFromBeginning[index] != tableOfTextFromEnd[index]):
        isTheSameLetter = False

print(isTheSameLetter)
