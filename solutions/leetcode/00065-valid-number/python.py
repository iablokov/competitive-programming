class Solution:
    def isNumber(self, s: str) -> bool:
        
        SYMBOLS = set(["e", "+", "-", "."])
        s = s.lower()

        # trivial checks
        if not all(c in SYMBOLS or c.isnumeric() for c in s) : return False
        if s.count(".") > 1 or s.count("e") > 1 : return False

        def check_int(n) : return len(n) > 0 and n.isnumeric()
        def del_signs(n) : return n[1:] if n and n[0] in ("+", "-") else n

        # first split: e/E
        n, e = s.split("e") if "e" in s else (s, "0")
        n, e = del_signs(n), del_signs(e)
        if not n or not e : return False

        # second split: .
        n, d = n.split(".") if "." in n else (n, "0")
        if not n and not d : return False
        if not d : d = "0"
        if not n : n = "0"

        return check_int(n) and check_int(e) and check_int(d)

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_isNumber_1(self):

        s = "0"
        expected = True
        output = Solution().isNumber(s)
        self.assertEqual(output, expected)

    def test_isNumber_2(self):

        s = "e"
        expected = False
        output = Solution().isNumber(s)
        self.assertEqual(output, expected)
    
    def test_isNumber_3(self):
            
        s = "."
        expected = False
        output = Solution().isNumber(s)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
