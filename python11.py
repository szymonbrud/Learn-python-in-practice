def checkTheFirstNumber(number): 
  listRange = list(range(1, number + 1))
  divisorList = []

  for n in listRange:
    if number % n == 0:
      divisorList.append(n)


  if len(divisorList) == 2:
    print("This is first number")
  else:
    print("This is NOT first number")

numInput = input("Input the number, I will say u that this is first number or it is not: ")

checkTheFirstNumber(int(numInput))
