import requests

def getNumbers():
    url = 'https://random-word-api.herokuapp.com/word?number=10'

    res = requests.get(url)
    content = res.json()
    return content

def saveToFile(dataToSave):
    file = open("python21_resolve.txt", "w")
    file.write(dataToSave)
    file.close()

def convertArrayToString(array):
    str1 = ""  

    for ele in array:  
        str1 += ele
        str1 += ', ' 
    
    return str1  
        
        
numbers = getNumbers()
saveToFile(convertArrayToString(numbers))



