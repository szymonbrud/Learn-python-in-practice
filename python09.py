import random
import os

clear = lambda: os.system('cls')

randomNumber = random.randint(1,9)

while True:
  clear()
  print('Input the number:\n')
  inputNumber = int(input())
  if randomNumber == inputNumber:
    print('U won!')
    break
  elif randomNumber > inputNumber:
    print('Liczba jest wieksza!')
  else:
    print('Liczba jest mniejsza!')
