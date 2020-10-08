with open('nameslist.txt', 'r') as file:
  content = file.readlines()
  print('there are ' + str(len(content)) + ' names in the file')
