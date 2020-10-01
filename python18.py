# 1. generete the number
# 2. ask user about number string, as soon as he don't win
# 3. said user score, and last string number

import random

def checkTheCodesIsEqual(mainCode, userCode):

    isTheSame = True

    for index in range(0,4):
        if mainCode[index] != userCode[index]:
            isTheSame = False
        
    return isTheSame

def checkDifferences(mainCode, userCode):
  bullsNumber = 0
  cowsNumber = 0

  for index in range(0,4):
    if mainCode[index] == userCode[index]:
      cowsNumber += 1

  for mainCodeElement in mainCode:
    for userCodeElement in userCode:
      if userCodeElement == mainCodeElement:
        bullsNumber += 1
  
  return bullsNumber
  
  # bullsNumber = bullsNumber - cowsNumber


# userCode = input('Wpisz 4 cyfrowy kod rozdzielony ","')

mainCode = []

testCode = []

# the bad way to create this like that because the numbers are repeatable

for n in range(0, 4):
    mainCode.append(random.randint(0,9))

for n in range(0, 4):
    testCode.append(random.randint(0,9))

resoult = checkDifferences(mainCode, testCode)
print(mainCode)
print(testCode)
print('-------')
print(resoult)
