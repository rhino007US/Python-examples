# collections: counter, namedtuple, orderedDict, defaultdict, deque
from collections import Counter
a = "aaaaabbbbccccdddd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.values())
print(my_counter.keys())
print(my_counter.most_common(1)) # returns a list with a tuple inside it
print(my_counter.most_common(1)[0][0]) # tuple at index 0, and just the element
# elements
print(list(my_counter.elements()))

# namedtuple
from collections import namedtuple # a namedtuple is an element type similar to a struct
Point = namedtuple('Point', 'x,y') # 'Point' is out namedtuple Class with elements x & y
pt = Point(1, -2)
print(pt)
print(pt.x, pt.y)

# orderedDict remembers the order of elements in a Dictionary, deprecated after python 3.7, dictionaries aren't ordered by default
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultdict 
from collections import defaultdict
d = defaultdict(int) # setting value to integer, could use float, list
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)
print(d['a'])
print(d['e']) # with a standard dictionary would return a key error, with defaultdict returns 0. the default integer

# deque a double ended queue
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)

d.pop()
d.popleft() # also d.clear() and d.extend()
print(d)
d.extend([4,5,6])
print(d)

d.extendleft([7,8,9]) # 9 will be the leftmost
print(d)

d.rotate(1)
print(d)














