import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value >= self.value
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value: #search right subtree
            if self.right is not None:
                return self.right.contains(target)
            else: 
                return False
        else: #target < self.value #search left subtree
            if self.left is not None:
                return self.left.contains(target)
            else: 
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        if self.right is not None:
            return self.right.get_max()
        else:
            return current_max
                    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.value is None:
            return

        if self.left is not None:
            self.left.in_order_print(self.left) 

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self) 
        while queue.size > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.size > 0:
            current = stack.pop()
            print(current.value)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if self.value is None:
            return

        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft(self.left) 

        if self.right is not None:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.value is None:
            return

        if self.left is not None:
            self.left.post_order_dft(self.left) 

        if self.right is not None:
            self.right.post_order_dft(self.right)

        print(self.value)

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            value = self.storage[0]
            self.storage = self.storage[1:]
            self.size -= 1
            return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            value = self.storage[self.size - 1]
            self.storage = self.storage[0:self.size - 1]
            self.size -= 1
            return value
        return None

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
#O(n^2)
for name_1 in names_1: #O(n)
    for name_2 in names_2: #O(n)
        if name_1 == name_2: #O(1)
            duplicates.append(name_1) #O(1)
"""

"""
#O(n) but uses built-in list
for name_1 in names_1:
    new_list.append(name_1)
for name_2 in names_2:
    if new_list.__contains__(name_2):
        duplicates.append(name_2)
"""
bst = BSTNode("root_value")
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.