from src.Matrix import Matrix

a = Matrix(2, 2, 'A', [
    [3, -2],
    [5, 6]
])

b = Matrix(2, 2, 'B', [
    [1, 3],
    [-2, 4]
])

c = a * b

print(c.toString())