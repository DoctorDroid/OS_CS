class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        old_head = self.head # Holds the or
        self.head = new_node
        self.head.next = old_head
    
    def remove_head(self):
        data = self.head.get_value()
        if self.head is None:
            return data
        self.head = self.head.next
        return data

    def remove_tail(self):
        data = self.tail.get_value()
        cursor = self.head
        while cursor.next.next is not None:
            cursor - cursor.next
        self.tail = cursor
        self.tail.next = None
        return data

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1  # self.size = self.size + 1 (same thing)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1 # self.size = self.size - 1 (same thing)
        return self.storage.remove_head()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_head()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # max_value = None
        # Can also set it to the first value in the tree, 
        #   but None accounts for the tree being empty.
        #   Can also add that condition
        # if max_value < self.value:
        #     max_value = self.value
        # The stuff above will not work if we use recursion

        # Recursion method
        # # Starting at the first value
        # max_value = self.value
        # # If the value is not None / If 
        current_node = self
        if current_node is None:
            return None

        while current_node.right:
            current_node = current_node.right

        max_value = current_node.value
        return max_value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_helper(self, node):
    #     if node is None:
    #         return
    #     BSTNode.in_order_helper(node.left)
    #     print(node.value)
    #     BSTNode.in_order_helper(node.right)

    # def in_order_print(self):
    #     BSTNode.in_order_helper(self)

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self)
        if self.right:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    ################ Still needs work ################
    # def bft_print(self):
    #     current_level = [node]
    #     while current_level:
    #         next_level = list()
    #         for node in current_level:
    #             print(node.value)
    #             if node.left:
    #                 next_level.append(node.left)
    #             if node.right:
    #                 next_level.append(node.right)
    #         print()
    #         current_level = next_level

    def bft_print(self):
        q = Queue()
        q.enqueue(self)
        while q.size != 0:
            current = q.dequeue()
            print(current.value)
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        s = Stack()
        s.push(self)
        while s.size != 0:
            current = s.pop()
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_helper(self, node):
    #     if node is None:
    #         return
    #     BSTNode.pre_order_helper(node.left)
    #     print(node.value)
    #     BSTNode.pre_order_helper(node.right)

    # def pre_order_dft(self):
    #     BSTNode.pre_order_helper(self)

    def pre_order_dft(self):
        if self:
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    # def post_order_helper(self, node):
    #     if node is None:
    #         return
    #     BSTNode.post_order_helper(node.left)
    #     BSTNode.post_order_helper(node.right)
    #     print(node.value)

    # def post_order_dft(self):
    #     BSTNode.post_order_helper(self)

    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
