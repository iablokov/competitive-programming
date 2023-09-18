from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        left     = 0    # `left` and `right` are sliding window indices 
        distinct = 0    # distinct charactes in the current sliding window      
        cnt = Counter() # character frequencies in the current sliding window

        max_len = 0

        for right, ch in enumerate(s):
            if cnt[ch] == 0 : distinct += 1
            cnt[ch] += 1
            while distinct > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0 : distinct -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_lengthOfLongestSubstringKDistinct_1(self):

        s = "eceba"
        k = 2
        expected = 3
        output = Solution().lengthOfLongestSubstringKDistinct(s, k)
        self.assertEqual(output, expected)

    def test_lengthOfLongestSubstringKDistinct_2(self):
        s = "aa"
        k = 1
        expected = 2
        output = Solution().lengthOfLongestSubstringKDistinct(s, k)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
