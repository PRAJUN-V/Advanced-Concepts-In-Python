# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# ---------- Counter ----------

a = 'aaabbbbbccccddddddd'
my_counter1 = Counter(a)
print(my_counter1) # Counter({'d': 7, 'b': 5, 'c': 4, 'a': 3})
print(dict(my_counter1)) # {'a': 3, 'b': 5, 'c': 4, 'd': 7}

b = [1, 1, 2, 3, 3, 3, 5, 5, 6, 6, 6, 6]
my_counter2 = Counter(b)
print(my_counter2) # Counter({6: 4, 3: 3, 1: 2, 5: 2, 2: 1})
print(my_counter2.most_common(2)) # [(6, 4), (3, 3)], Return 2 most common type.

# ----------- namedtuple ----------

Point = namedtuple('Point', 'x, y') # Point is the class name and x and y is fields.
pt1 = Point(2, 3)
pt2 = Point(-1, 1)
print(pt1)
print(pt1.x)

# ----------- OrderedDict ----------
# It is just like the regular dict, but it remembers the order which the item is inserted.
# But new version of dict also is ordered so we don't need to use this if our python version is not old.

ordered_dict = OrderedDict()
ordered_dict[1] = 'a'
ordered_dict[2] = 'b'
ordered_dict[3] = 'c'
ordered_dict[4] = 'd'
print(ordered_dict)


# ---------- defaultdict ----------
# It is also similar to default dict but the only difference is it will have a default value if the key has not been set yet.

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['c']) # If key is not found it will return a default value 0 for int.

# ---------- deque ----------
# double ended queue
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d.clear()
d.extend([4, 5, 6])
d.extendleft([7, 8, 9])
d.rotate(2)
d.rotate(-1)
print(d)
