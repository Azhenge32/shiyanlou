squares = []
for x in range(10):
    squares.append(x ** 2)
print(x) # x变量作用域过大
print(squares)
squares = list(map(lambda  x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
print(combs)
combs =  [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

a=[1, 2, 3]
z = [x + 1 for x in [x ** 2 for x in a]]
print(z)