from typing import Optional
from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node: Optional[TreeNode], acc: int, stack: list[int], paths: list[list[int]]):
            if not node : return []
            
            stack.append(node.val)
            acc += node.val
            if not node.left and not node.right:
                if acc == targetSum : paths.append(list(stack))
            else:
                dfs(node.left,  acc, stack, paths)
                dfs(node.right, acc, stack, paths)
            stack.pop()

            return paths
        
        return dfs(root, 0, [], [])


#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    ## TO BE IMPLEMENTED
    def test_pathSum_1(self):
        pass            

if __name__ == '__main__':
    unittest.main()
