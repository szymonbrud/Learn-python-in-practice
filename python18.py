# 1. generete the number
# 2. ask user about number string, as soon as he don't win
# 3. said user score, and last string number

import random

def checkTheCodes(mainCode, userCode):

    isTheSame = True

    for index in range(0,4):
        if mainCode[index] !== userCode[index]:
            isTheSame = False
        
    return isTheSame

# userCode = input('Wpisz 4 cyfrowy kod rozdzielony ","')

mainCode = []

for n in range(0, 4):
    mainCode.append(random.randint(0,9))

    


# def askUserAboutNumbers():
    
