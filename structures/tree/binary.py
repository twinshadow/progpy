class Node (object):
    def __init__ (self,
                  data = None,
                  lt = None,
                  gt = None ):

        self.data = data
        self.lt   = lt
        self.gt   = gt

    def __str__ (self):
        return str (self.data)

    def __len__ (self):
        sum = 0

        if self.lt:
            sum += self.lt.count ()

        if self.gt:
            sum += self.gt.count ()

        return sum + 1

    def insert (self, *args):
        for num in args:
            if (num < self.data):
                if (self.lt is None):
                    self.lt = Node(num)
                else:
                    self.lt.insert (num)
            else:
                if (self.gt is None):
                    self.gt = Node(num)
                else:
                    self.gt.insert (num)

    def inorder (self, func):
        if self.lt: self.lt.inorder (func)
        func (self)
        if self.gt: self.gt.inorder (func)

    def preorder (self, func):
        func (self)
        if self.lt: self.lt.preorder (func)
        if self.gt: self.gt.preorder (func)

    def postorder (self, func):
        if self.lt: self.lt.postorder (func)
        if self.gt: self.gt.postorder (func)
        func (self)

class Tree (object):
    def __init__ (self,
                  trunk = None ):

        self.trunk = trunk

