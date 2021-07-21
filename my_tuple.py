import sys

# tuples
# my_tuple = (0, 1, 2, 3, 4)

# i1, *i2, i3 = my_tuple

# print(i1)
# # print(i2)
# print(i3)

#getsizeof

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

