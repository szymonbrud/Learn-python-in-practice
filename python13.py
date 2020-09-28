def generateFibonacci(lenghtOfFibonacci):

    fullString = [1, 1]

    def addOneMore():
        fullString.append(
            fullString[len(fullString) - 1] + fullString[len(fullString) - 2])

    for n in range(0, lenghtOfFibonacci):
        if n > 1:
            addOneMore()
        print(str(n + 1) + '. ' + str(fullString[n]))


lenghtOfFibonacci = int(input('How log fibonacci do u want to: '))
generateFibonacci(lenghtOfFibonacci)
