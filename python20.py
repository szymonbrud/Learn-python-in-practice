array1 = [1,2,3,4,7,10,21,30,45]

def findInArray(numberToFind):
    for arrayElement in array1:
        if(arrayElement == numberToFind):
            return 'Finded!!'
    return 'Not finded'

print(findInArray(18))
