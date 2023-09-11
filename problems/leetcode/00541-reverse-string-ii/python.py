class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s, n = list(s), len(s)

        for i in range(0, n, 2*k):
            j = min(i + k, n)
            s[i:j] = reversed(s[i:j])  # in-place reverse on a slice
            
        return "".join(s)
    
#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_reverseStr_1(self):

        s, k = "abcdefg", 2
        expected = "bacdfeg"
        output = Solution().reverseStr(s, k)
        self.assertEqual(output, expected)

    def test_reverseStr_2(self):
        s, k = "abcd", 2
        expected = "bacd"
        output = Solution().reverseStr(s, k)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
