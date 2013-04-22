numbers_file = open('numbers.txt')
data = True
while data:
    data = numbers_file.readline()
    # data = numbers_file.next()
    print(data)
    
  
for line in numbers_file:
    print(line)


---


%run 02.03.02.fibiter.py

f = Fib()
f.next()
f.next()
f.next()
f.next()
f.next()