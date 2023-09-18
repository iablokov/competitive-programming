from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        node = dummy = ListNode(0, head)
        
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        
        return dummy.next
    
#==============================================================================

import unittest

def list_to_linked_list(node_vals):
    node = dummy = ListNode(0)
    for n in node_vals:
        node.next = ListNode(n)
        node = node.next
    return dummy.next

def linked_list_to_list(head):
    node_vals = []
    node = head
    while node:
        node_vals.append(node.val)
        node = node.next
    return node_vals

class TestSolution(unittest.TestCase):

    def test_removeElements_1(self):

        node_vals_inp = [1,2,6,3,4,5,6]
        node_vals_exp = [1,2,3,4,5]
        val = 6
        
        head = list_to_linked_list(node_vals_inp)
        head = Solution().removeElements(head, val)
        node_vals_out = linked_list_to_list(head)

        self.assertEqual(node_vals_exp, node_vals_out)

    def test_removeElements_2(self):
            
        node_vals_inp = []
        node_vals_exp = []
        val = 1
        
        head = list_to_linked_list(node_vals_inp)
        head = Solution().removeElements(head, val)
        node_vals_out = linked_list_to_list(head)

        self.assertEqual(node_vals_exp, node_vals_out)

    def test_removeElements_3(self):
            
        node_vals_inp = [7,7,7,7]
        node_vals_exp = []
        val = 7
        
        head = list_to_linked_list(node_vals_inp)
        head = Solution().removeElements(head, val)
        node_vals_out = linked_list_to_list(head)

        self.assertEqual(node_vals_exp, node_vals_out)

if __name__ == '__main__':
    unittest.main()
