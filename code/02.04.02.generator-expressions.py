# Example 2: Generator expressions
# Mostrar em ipython
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
G = (sum(row) for row in M)
G
G.next()
G.next()
G.next()

map(sum, M)
