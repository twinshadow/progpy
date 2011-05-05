import sys
if '' not in sys.path: sys.path.insert (0, '')

import structures.list.single_link
import structures.list.double_link

class Test_Sanity (object):
    def test_num (self):
        assert (1 + 1) == 2

class Test_Lists (object):
    def test_single_node (self):
        node = structures.list.single_link.Node(5)
        assert node is not None

    def test_double_node (self):
        node = structures.list.double_link.Node()
        assert node.data is None
