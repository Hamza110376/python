A= {1,2,3}
B={3,4,5}

# methods
# s.add(4)
# s.remove(3)
# s.discard(3)
# s.pop()
# s.clear()

# some operaation on sets

union_set= A.union(B)
print(union_set)

intersection_set = A.intersection(B)
print(f"the intersection of set is {intersection_set}")

difference_set= A.difference(B)
print(f"the difference of set is {difference_set}")

sym_diff = A.symmetric_difference(B)
print(f"the symmetric difference of set is {sym_diff}")
