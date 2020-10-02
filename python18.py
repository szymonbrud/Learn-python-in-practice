import random
import os


def clear(): return os.system('cls')


historyOfType = []
historyOfScores = []


def generateCode():
    code = []

    for index in range(0, 4):
        while True:
            isRepeat = False

            randomNumber = random.randint(0, 9)

            for codeElement in code:
                if codeElement == randomNumber:
                    isRepeat = True

            if isRepeat == False:
                code.append(randomNumber)
                break

    return code


def checkDifferences(mainCode, userCode):
    bullsNumber = 0
    cowsNumber = 0

    for index in range(0, 4):
        if mainCode[index] == userCode[index]:
            cowsNumber += 1

    for mainCodeElement in mainCode:
        for userCodeElement in userCode:
            if userCodeElement == mainCodeElement:
                bullsNumber += 1

    bullsNumber = bullsNumber - cowsNumber
    return [bullsNumber, cowsNumber]


def askUser():
    print('Type code like: 1325')
    [one, two, three, four] = input('Type code here: ')
    userCodeString = [one, two, three, four]
    userCodeInt = list(map(int, userCodeString))
    historyOfType.append(userCodeInt)
    return userCodeInt


def response(bulls, cows):

    clear()
    for index in range(0, len(historyOfType)):
        print(str(index + 1) + '.', historyOfType[index], 'bulls:',
              historyOfScores[index][0], 'cows:', historyOfScores[index][1])

    print('\n')
    print('Bulls: ' + str(bulls))
    print('Cows: ' + str(cows))


def main():
    mainCode = generateCode()

    while True:

        userCode = askUser()

        [bulls, cows] = checkDifferences(mainCode, userCode)

        historyOfScores.append([bulls, cows])

        win = cows == 4
        if(win):
            print('U won!')
            break
        else:
            response(bulls, cows)


main()
