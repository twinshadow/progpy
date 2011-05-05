class Node (object):
    def __init__ (self, num = 0, next = None):
        self.data = num
        self.next = next

    def __str__ (self):
        return str (self.data)

class List (object):
    "List: A meta-object that provides the 'head' attribute and several functions for working with linked-lists"
    def __init__ (
                    self,
                    head  = None,
                    tail  = None,
                    count = None
                 ):

        self.head  = head
        self.tail  = tail
        self.count = count

    def __str__ (self):
        "echo: print all the Nodes in the attached list"
        node = self.head

        while (node is not None):
            print node
            node = node.next

    def reverse (self):
        "reverse: alter the list by reversing the order"
        node = self.head
        stack = None

        while (node is not None):
            hold = node
            node = node.next
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

