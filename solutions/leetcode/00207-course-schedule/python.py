from collections import deque

class Solution:
    def canFinish(self, n: int, edges: list[list[int]]) -> bool:

        G = { u: list() for u in range(n)}
        for u,v in edges : G[v].append(u)

        def in_degree(G: dict[int,list[int]]) -> dict[int,int]:
            ''' Compute the in-degree of each vertex in G. '''
            deg = { u : 0 for u in range(len(G))}
            for u, vs in G.items():
                for v in vs : deg[v] += 1
            return deg

        def is_dag(G: dict[int,list[int]]) -> bool:
            ''' Return True if G is a DAG, False otherwise. '''

            n = len(G)
            D = in_degree(G)
            Q = deque([u for u,c in D.items() if c == 0])
            
            while Q:
                u = Q.popleft()
                n -= 1
                if n == 0 : return True

                for v in G[u]:
                    D[v] -= 1
                    if D[v] == 0:
                        Q.append(v)
        
            return False
        
        return is_dag(G)

#==============================================================================

import unittest

class TestSolution(unittest.TestCase):

    def test_canFinish_1(self):

        n = 2
        edges = [[1,0]]
        expected = True
        output = Solution().canFinish(n, edges)
        self.assertEqual(output, expected)

    def test_canFinish_2(self):
            
        n = 2
        edges = [[1,0],[0,1]]
        expected = False
        output = Solution().canFinish(n, edges)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
