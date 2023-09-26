from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(s: str, o: int, c: int, combs: list):
            if o == c and o == n : combs.append(s)
            if o < n : dfs(s + "(", o+1, c, combs)
            if c < o : dfs(s + ")", o, c+1, combs)
            return combs

        return dfs("", 0, 0, [])

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_generateParenthesis_1(self):

        n = 3
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        output = Solution().generateParenthesis(n)
        self.assertEqual(output, expected)

    def test_generateParenthesis_2(self):

        n = 1
        expected = ["()"]
        output = Solution().generateParenthesis(n)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
