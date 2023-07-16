set1 = {10,20,10,10,(10,10)}


# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
print(set1)   # {(10, 10), 10, 20}

# Set -> Unordered (Unindexed), 

set1.add(102)
print(set1)   # {(10, 10), 10, 20, 102}

set1.update([555, 89982, 555])
print(set1)   # {102, 10, 555, (10, 10), 20, 89982}

set1.remove(10)
print(set1)


set1.discard(500)

set1.pop()
set1.pop()
print(set1)


set1 = {10,20,30,40}
set2 = {40,50,60}

print(set1.difference(set2))   # {10,20,30}


print(set1.symmetric_difference(set2))  # {10, 50, 20, 60, 30}


print(set1.intersection(set2))   # {40}

set1 = {10,20,30,40}
set2 = {20,30}


print(set1.isdisjoint(set2))   # True
print(set1.issubset(set2))   # False
print(set1.issuperset(set2))  # True