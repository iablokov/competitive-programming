from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        node_copy = dummy = Node(0)
        node_orig = head

        # copy list and map nodes to copies
        node_map = {}
        while node_orig:
            node_copy.next = Node(node_orig.val, None, node_orig.random)
            node_map[node_orig] = node_copy.next
            node_copy = node_copy.next
            node_orig = node_orig.next

        # remap original random links to the copied ones
        node_copy = dummy.next
        while node_copy:
            node_copy.random = node_map.get(node_copy.random, None)
            node_copy = node_copy.next
        
        return dummy.next    
#==============================================================================

import unittest

def list_to_random_linked_list(lst: list):
    nodes = []
    for val, _ in lst : nodes.append(Node(val))
    for i, (_, rnd) in enumerate(lst):
        nodes[i].next   = nodes[i+1] if i+1 < len(lst) else None
        nodes[i].random = nodes[rnd]
    return nodes[0] if nodes else None

class TestSolution(unittest.TestCase):

    ### TO BE IMPLEMENTED !

    def test_copyRandomList_1(self):
        pass


if __name__ == '__main__':
    unittest.main()
