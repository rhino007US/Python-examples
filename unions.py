# unions & intersections of sets
odds = {1,3,5,7,9}
evens = {2,4,6,8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

ep = evens.union(primes)

print(ep)

i = evens.intersection(primes)
print(i)

x = odds.intersection(primes)
print(x)

SetA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
SetB = {1, 2, 3, 10, 11, 12}

diff = SetA.difference(SetB)
print(diff)

diff2 = SetB.difference(SetA)
print(diff2)

diff3 = SetB.symmetric_difference(SetA)
print(diff3)

diff4 = SetA.symmetric_difference(SetB)
print(diff4)

# SetA.update(SetB) takes all the elements in SetA and updates them with the unique elements in Setb
# SetA.intersection(SetB) takes all the elements from SetA and adds any elements (without duplication) in setB
# SetA.intersection_update(SetB) only the elements appearing in both sets
# SetA.difference_update(SetB) only the elements that are different in SetA and SetB, removing new elements in SetB
SetA.symmetric_difference_update(SetB)
print(SetA)

print(SetA.issubset(SetB))
print(SetA.issuperset(SetB)) # True is SetA contains all the elements of SetB
print(SetA.isdisjoint(SetB))

SetC = {13,14,15}
print(SetA.isdisjoint(SetC))

SetD = SetC.copy()
SetD.add(7)

print(SetC)
print(SetD)

a = frozenset([1, 2, 3, 4])
a.add(5)

print(a)







