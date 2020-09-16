a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

outTable = []

isDuplicate = False

for elementA in a:
    for elementB in b:
        if elementA == elementB:
            for elementOut in outTable:
                if(elementA == elementOut):
                    isDuplicate = True
    
    if isDuplicate == False:
        outTable.append(elementA)
    else:
        isDuplicate = False


print(outTable)
