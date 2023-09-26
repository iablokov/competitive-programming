from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        
        l = r = bisect_left(arr, x)

        while r - l < k:

            if l == 0        : return arr[:k]
            if r == len(arr) : return arr[-k:]

            if abs(arr[l-1]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
        
        return arr[l:r]
    
#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_findClosestElements_1(self):

        arr      = [1,2,3,4,5]
        k, x     = 4, 3 
        expected = [1,2,3,4]
        output   = Solution().findClosestElements(arr, k, x)
        self.assertEqual(output, expected)

    def test_findClosestElements_2(self):

        arr      = [1,2,3,4,5]
        k, x     = 4, -1 
        expected = [1,2,3,4]
        output   = Solution().findClosestElements(arr, k, x)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
