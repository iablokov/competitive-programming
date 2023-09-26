from typing import Optional
from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # idea: a tree is a bunch of lists with shared prefixes
        #       solve the problem for list, generalize for tree

        def dfs(node: Optional[TreeNode], acc: int, cnt: Counter) -> int:
            
            if not node : return 0

            acc += node.val                     # maintaining a prefix sum
            paths = cnt[acc-targetSum]          # counting paths that end here
            cnt[acc] += 1
            paths += dfs(node.left, acc, cnt)   # counting paths that end at 
            paths += dfs(node.right, acc, cnt)  # left and right child nodes
            cnt[acc] -= 1

            return paths

        return dfs(root, 0, Counter([0]))


#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    ## TO BE IMPLEMENTED
    def test_pathSum_1(self):
        pass            

if __name__ == '__main__':
    unittest.main()
