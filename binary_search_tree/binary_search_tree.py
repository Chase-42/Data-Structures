from stack import Stack
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Check if value is les than current node's value
        if value < self.value:
            # If yes does it have a left child? 
            if self.left: 
                # Recursively call .inesrt() 
                self.left.insert(value)
            else: 
                # If no child put it here
                self.left = BSTNode(value)
        # Check if value is greater than or equal to curren node's value
        if value >= self.value:
            # If yes, does it have a right child? 
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    
    def contains(self, target):
        # Check the root
        if target == self.value:
            return True
        # Check left nodes:
        elif target < self.value and self.left:
                # Recursively call .contains()
                return self.left.contains(target) 
        # Check right nodes:
        elif target > self.value and self.right:
                # Recursively call .contains()
                return self.right.contains(target) 
        else: 
            return False

    # Return the maximum value found in the tree
    def get_max(self):
         # Check if empty
        if not self:
            return
        # If a single-node 
        if not self.right:
            return self.value
        # Else if a multi-level 
        else: 
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Check if empty
        if not self:
            return
        # Check if root
        if self:
            fn(self.value)
        # Check if right nodes
        if self.right is not None:
            self.right.for_each(fn)
        # Check if left nodes
        if self.left is not None:
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if node is not None:
            self.in_order_print(node.left) #left
            print(node.value) #root
            self.in_order_print(node.right) #right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while len(queue) > 0:
            removed = queue.dequeue()
            # Print root
            print(removed.value)
            # Check if left
            if removed.left:
                queue.enqueue(removed.left)
            # Check if right
            if removed.right:
                queue.enqueue(removed.right)

                
            
      
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            popped = stack.pop()
            # Print root
            print(popped.value)
            # Check if left
            if popped.left:
                stack.push(popped.left)
            # Check if right
            if popped.right:
                stack.push(popped.right)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            # Pre-order print
            print(node.value)
            # Recurisvely call on left
            self.pre_order_dft(node.left)
             # Recurisvely call on left
            self.pre_order_dft(node.right)
            

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            # Recurisvely call on left
            self.post_order_dft(node.left)
            # Recurisvely call on right
            self.post_order_dft(node.right)
            # Post-order print
            print(node.value)

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(5)
# bst.insert(7)
# bst.insert(3)
# bst.insert(2)
# bst.insert(4)

bst = BSTNode(8)
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)

# bst.in_order_print()
bst.bft_print(bst)
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  