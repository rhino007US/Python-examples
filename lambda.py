# lambda arguemnts: expression

add10 = lambda x: x + 10
print(add10(5))

# same as
def add10_func(x):
    return x + 10
print(add10_func(5))

mult = lambda x,y: x*y
print(mult(2,7))

points2d = [(1,2), (15,1), (5,-1), (10,4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])

print(points2d_sorted)

# map function
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# filter(func, seq) function 
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2 ==0] # same thing without lambda
print(c)

# reduce(func, seq)
from functools import reduce
a = [1,2,3,4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
