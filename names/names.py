import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
def append_duplicates_slow():
    # runtime complexity O(n*m) ~= O(n^2)
    for name_1 in names_1: # n
        for name_2 in names_2: # m
            if name_1 == name_2:
                duplicates.append(name_1)

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value and self.right:
            return self.right.contains(target)
        if target < self.value and self.left:
            return self.left.contains(target)
        return False

def append_duplicates_fast():
    # runtime complexity O(m + n*log n) ~= O(n*log n)
    names_2_tree = BinarySearchTree()
    for name_2 in names_2: # m
        names_2_tree.insert(name_2)
    for name_1 in names_1: # n
        if names_2_tree.contains(name_1): # log n
            duplicates.append(name_1)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

def append_duplicates_stretch():
    duplicates.extend(set(names_1).intersection(names_2))

# append_duplicates_slow()
# append_duplicates_fast()
append_duplicates_stretch()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
