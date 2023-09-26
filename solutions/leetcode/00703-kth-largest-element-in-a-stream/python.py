import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.k = k
        for n in nums : self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
    
#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_kth_largest(self):

        k        = 3
        nums     = [4,5,8,2]
        stream   = [3,5,10,9,4]
        expected = [4,5,5,8,8]

        obj = KthLargest(k, nums)
        output = [obj.add(n) for n in stream]
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
