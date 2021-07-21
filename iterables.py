# itertools: product, permutations, combinations, accumlate, groupby, and infinite iterators
from itertools import groupby, product
a = [1, 2]
b = [4, 5]
prod = product(a, b, repeat=2) # repeat is optional
print(list(prod))
print("*** permutations ***")
# permutations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a) # optional length integer after a
print(list(perm))

# combinations & combinations_with_replacement
print("*** combinations ***")
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a,2)
print(list(comb))
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

print("*** accumulate ***")
# accumulate function
from itertools import accumulate
import operator  # for 2nd excample below
a = [1, 2, 5, 3, 4]
acc = accumulate(a) # optional other math like "func-operator.mul" for multiplication
# acc = accumulate(a, func=operator.mul)
# acc = accumulate(a, func=max) will figure out that 5 is the max
print(a)
print(list(acc))
print("**** groupby ****")
# groupby returns a key
from itertools import groupby

# def smaller_than_3(x):
#   return x < 3

a = [1, 2, 3, 4]
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 27},
           {'name': 'Lisa', 'age': 36}, {'name': 'Clair', 'age': 28}]
# group_obj = groupby(a, key=smaller_than_3) requires the def above
# for key, value in group_obj:
#    print(key, value)
group_obj = groupby(persons, key=lambda x: x['age']) # lambda doesn't require the def above
for key, value in group_obj:
    print(key, list(value))
print("*** count ***")
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

i = [1, 2, 3]
for i in cycle(i):
    print(i)
