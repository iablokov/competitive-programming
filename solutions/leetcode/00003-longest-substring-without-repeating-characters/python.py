from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start   : int = 0       # `start` is the position of the last
        max_len : int = 0       # occurence of all characters that
        pos = defaultdict(int)  # were seen so far in the for-cycle
        
        for end, ch in enumerate(s):
            start   = max(start, pos[ch])
            max_len = max(max_len, end-start+1)
            pos[ch] = end + 1
                
        return max_len

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_lengthOfLongestSubstring_1(self):

        s = "abcabcbb"
        expected = 3
        output = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(output, expected)

    def test_lengthOfLongestSubstring_2(self):
        s = "bbbbb"
        expected = 1
        output = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(output, expected)

    def test_lengthOfLongestSubstring_3(self):
        s = "pwwkew"
        expected = 3
        output = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
