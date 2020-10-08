with open('happynumbers.txt') as fp, open('primenumbers.txt') as fp2: 
  file1Lines = fp.read().splitlines()
  file2Lines = fp2.read().splitlines()

  repeatNumbers = []

  for happyNumber in file1Lines:
    for primeNumber in file2Lines:
      if happyNumber == primeNumber:
        repeatNumbers.append(happyNumber)

  print(repeatNumbers)