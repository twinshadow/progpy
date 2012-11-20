class Node (object):
    def __init__ (
                    self,
                    data = None,
                    prev = None,
                    next = None
                 ):

        self.data = data
        self.prev = prev
        self.next = next

    def __str__ (self):
        return str (self.data)

class List (object):
    def __init__ (
                    self,
                    head = None,
                 ):

        self.head = head

    def __str__ (self):
        return str (self.count)

    def pop (self):
        node = self.head

        self.head = self.head.next
        self.head.prev = None

        return node

    def push (self, data):
        node = Node (data, None, self.head)

        self.head.prev = node
        self.head = node

    def recount (self):
        pass

    def reverse (self):
        pass

    def sort (self):
        pass

