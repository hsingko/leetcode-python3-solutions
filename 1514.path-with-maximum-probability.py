#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[0 for _ in range(n)] for _ in range(n)]
        for idx, edge in enumerate(edges):
            i, j = edge
            adj[i][j] = succProb[idx]
            adj[j][i] = succProb[idx]
        heap = [(1,0)]
        visited = set()
        probs = [0]*n
        probs[0] = 1
        while heap:
            poss, curr = heappop(heap)
            if curr in visited:
                continue
            visited.add(curr
            )
            for neig, prob in enumerate(adj[curr]):
                if prob > 0:
                    probs[neig] = max(probs[neig], prob*poss)
                    heappush(heap, (probs[neig], neig))
        return probs[n-1]

# @lc code=end

