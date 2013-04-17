def fibonacci(max_value):
    a, b = 0, 1
    while a < max_value:
        yield a
        a, b = b, a+b

f = fibonacci(1000)
f.next()

for n in fibonacci(1000):
    print n
    
---

G = (sum(row) for row in M)
map(sum, M)