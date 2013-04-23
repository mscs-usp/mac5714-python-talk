numbers_file = open('numbers.txt')
data = True
while data:
    data = numbers_file.readline()
    # data = numbers_file.next()
    print(data)
    
  
for line in numbers_file:
    print(line)
