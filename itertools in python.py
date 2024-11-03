# itertools : product, permutations, combinations, groupby and infinite iterators

# ---------- product ----------

from itertools import product, permutations, combinations

a = [1, 2]
b = [3, 4]
prod = product(a, b) # cartesian product
print(list(prod))

# ---------- permutations -----------

c = [1, 2, 3]
perm = permutations(c)
perm2 = permutations(c, 2)
print(list(perm))
print(list(perm2))

# ---------- combinations ----------

d = [1, 2, 3]
perm3 = combinations(d, 2)
print(list(perm3))
