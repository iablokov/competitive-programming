import unittest
from itertools import takewhile

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        return "".join(ch[0] for ch in takewhile(lambda c: len(set(c))==1, zip(*strs)))

#==============================================================================

class TestSolution(unittest.TestCase):

    def test_longestCommonPrefix_1(self):

        strs = ["flower","flow","flight"]
        expected = "fl"
        output = Solution().longestCommonPrefix(strs)
        self.assertEqual(output, expected)

    def test_longestCommonPrefix_2(self):
        strs = ["dog","racecar","car"]
        expected = ""
        output = Solution().longestCommonPrefix(strs)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
