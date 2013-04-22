# Example 1: Using the yield statement
def fibonacci(max_value):
    a, b = 0, 1
    while a < max_value:
        yield a
        a, b = b, a+b

f = fibonacci(1000)
f.next()

for n in fibonacci(1000):
    print n
    
###

# Example 1: Generator expression
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
G = (sum(row) for row in M)
G
G.next()
G.next()
G.next()

map(sum, M)