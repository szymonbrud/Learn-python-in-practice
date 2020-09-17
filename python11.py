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

checkTheFirstNumber(11)
