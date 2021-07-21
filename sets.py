setone = {4,5,6,7,5,6}
print(setone)

myset = set() # casting to set even with  "()"

myset.add(1)
myset.add(2)
myset.add(3)

print(type(myset))
print(myset)
for i in myset:
   print (i)

myset.remove(2)

print(myset)

# myset.clear()
myset.pop()

print(myset)





