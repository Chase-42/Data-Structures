from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

"""1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass."""
"""class Stack:
     def __init__(self):
         self.size = 0
         self.storage = []

     def __len__(self):
         return len(self.storage)

     def push(self, value):
         return self.storage.append(value)

     def pop(self):
         if len(self.storage) < 1:
             return None
         else:
             return self.storage.pop()"""

"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None

'''
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   An array is a random access data structure. A linked list is a sequential access data structure. 
   Thus the methods you use to add and remove elements are different. 
   
'''









