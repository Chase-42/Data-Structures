"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Wrap the value in a list node 
        new_node = ListNode(value)
        # Check if it is empty
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # Else if it is not empty
        else:
        # Set new head's next node to the old head
            new_node.next = self.head
        # Set head to the new node 
            self.head.prev = new_node 
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        if not self.head: 
            return None
        
        removed_value = self.head.value
        self.length -= 1 

        if self.head.next != None:
            self.head = self.head.next

        else:
            self.head = None
            self.tail = None

        return removed_value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        new_node = ListNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1 

        else: 
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass