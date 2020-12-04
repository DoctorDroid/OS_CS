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
        new_node = ListNode(value)
        old_head = self.head
        # You only need need to actual use `new_node.next = self.head` 
        #   but this helps to know what is going on better
        new_node.next = old_head 

        # Since there was nothing in the list before this, this becomes the entire list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Below is the same as `self.head.prev = new_node`
        old_head.prev = new_node

        # Moves the pointer (head) to the "front".
        # Head is just a variable we use for our computer to point where we want to start
        self.head = new_node
        self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return

        value = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value    

        new_head = self.head.next
        self.head = new_head
        self.head.prev = None
        self.length -= 1
        
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
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
        if self.head is None:
            return
        
        if self.head is node:
            return

        if self.tail != node:
            node.next.prev = node.prev

        else:
            self.tail = node.prev

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is None:
            return
        
        if self.tail is node:
            return
        
        if self.head != node:
            node.prev.next = node.next
        
        else:
            self.head = node.next
        
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            return
        
        if self.head is self.tail and self.head is node:
            self.head = None
            self.tail = None
            self.length = 0
            return
        
        if self.head is node:
            self.head = node.next
            self.head.prev = None
            self.length -= 1
            return
        
        elif self.tail is node:
            self.tail = node.next
            self.tail.next = None
            self.length -= 1
            return
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value
        pointer = self.head

        while pointer is not None:
            if max_value < pointer.value:
                max_value = pointer.value
            
            pointer = point.next

        return max_value