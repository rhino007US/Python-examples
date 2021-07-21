# strings: ordered, immutable, text, representation
from timeit import default_timer as timer
my_string = "Hello "
name = "Tom"
substring = my_string[::] # first char, last char, increment/decrement
print(substring)
sentence = my_string + name
print(sentence)

for e in my_string:
    print("yes")
else:
   print("no")

my_string1 = "    Hello World   "
print(my_string1)
my_string1 = my_string1.strip()
print(my_string1.upper())

# also lower(), startswith(), endswith(), find('o')
print(my_string1.find('o'))
print(my_string1.replace('World', 'Tom'))

# strings & lists
my_string2 = "how are you doing"
my_list = my_string2.split(" ")
print(my_list) # string converted to list
# convert list back to string
new_string = ' '.join(my_list)
print(new_string)

my_list2 = ['a'] * 6
print(my_list2)

# bad
start = timer()
my_string3 = ''
for i in my_list2:
    my_string3 += i
    stop = timer()
print(stop-start)
print(my_string3)

# good
start = timer()
my_string4 = ''.join(my_list2)
stop = timer()
print(stop-start)
print(my_string4)

   

