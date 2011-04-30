class Node (object):
    def __init__ (self, num = 0, next = None):
        self.data = num
        self.next = next

class List (object):
    "List: A meta-object that provides the 'head' attribute and several functions for working with linked-lists"
    def __init__ (self, head = None):
        self.head = head

    def echo (self):
        "echo: print all the Nodes in the attached list"
        link = self.head

        while (link is not None):
            print link.data
            link = link.next

    def reverse (self):
        "reverse: alter the list by reversing the order"
        link = self.head
        stack = None

        while (link is not None):
            hold = link
            link = link.next
            hold.next = stack
            stack = hold

        self.head = stack

#        def sort (self):
#            "sort: sort the list from largest to smallest"
#            link = self.head
#            stack = None
#
#            while (link is not None):
#                pop = link
#                link = link.next 

    def unshift (self, num):
        "unshift: Create a new node at the beginning of the List"
        node = Node(num)
        node.next = self.head
        self.head = node

