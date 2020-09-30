import random

def generatePassword():
  password = ''
  for n in range(1, 15):
    randomNumber = random.randint(33,126)
    password = password + chr(randomNumber)
    
  return password

print(generatePassword())
