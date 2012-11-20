class Node (object):
    def __init__ (self, num = 0, next = None):
        self.data = num
        self.next = next

    def __str__ (self):
        return str (self.data)

    def __len__ (self):
        count = len(self.next) + 1 if self.next else 1
        return count

class List (object):
    "List: A meta-object that provides the 'head' attribute and several functions for working with linked-lists"
    def __init__ (
                    self,
                    head  = None,
                 ):
        self.head  = head

    def __str__ (self):
        node = self.head
        while node:
            print node
            node = node.next

    def __len__ (self):
        return len(self.head) if self.head else 0

    def __nonzero__ (self):
        return 1 if self.head else 0

    def __getitem__ (self, k):
        len = self.__len__()
        count = 0
        node = self.head

        if isinstance(k, slice):
            start = k.start if k.start else 0
            step = k.step if k.step else 0
            stop = k.stop if k.stop else 0

            stack = None
            while node:
            return stack
        else:
            if k < 0:
                k += len
                if k < len: raise IndexError("list index out of range")
            if k > len: raise IndexError("list index out of range")

            while node:
                if count == k: return Node(node.data)
                count += 1
                node = node.next

    def __setitem__ (self, k, v):
        pass

    def __contains__ (self, v):
        node = self.head
        while node:
            if node.data == v:
                return 1
            else: node = node.next
        return 0

    def __reversed__ (self):
        node = self.head
        stack = None
        while node is not None:
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

