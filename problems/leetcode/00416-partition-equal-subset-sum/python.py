from functools import cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        full_sum, n = sum(nums), len(nums)

        if full_sum %2 != 0 : return False

        nums.sort()

        @cache
        def dfs(i, s):
            if s == 0 : return True
            if s <  0 : return False
            if i == n : return False
            return dfs(i+1, s) or dfs(i+1, s-nums[i])

        return dfs(0, full_sum // 2)

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_canPartition_1(self):

        nums = [1,5,11,5]
        expected = True
        output = Solution().canPartition(nums)
        self.assertEqual(output, expected)

    def test_canPartition_2(self):
        nums = [1,2,3,5]
        expected = False
        output = Solution().canPartition(nums)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
