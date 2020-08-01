import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
"""

with open('names_2.txt', 'r') as n2:
    line = n2.readline().strip()
    tree = None
    while line:
        if tree == None:
            tree = BSTNode(line)
        else:
            tree.insert(line)
        print(f'read: {line}')
        line = n2.readline().strip()

duplicates = []  # Return the list of duplicates in this data structure

"""
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

for name in names_1:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

"""
Runtime of original code on my machine:  5.6630449295043945 seconds
Runtime of optimized code on my machine: 0.24960613250732422 seconds
"""

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
