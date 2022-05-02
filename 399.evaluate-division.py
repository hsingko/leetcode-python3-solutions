#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            val = values[i]
            path[a][b] = val
            path[b][a] = 1/val
        result = []

        def query(x, y):
            if x not in path:
                return -1
            visited = set()
            stack = [(x,1)]
            while stack:
                curr, acc = stack.pop()
                if curr == y:
                    return acc
                if curr in visited:
                    continue
                visited.add(curr)
                for neig,val in path[curr].items():
                    stack.append((neig, val*acc))
            return -1

        for x,y in queries:
            result.append(query(x, y))
        return result


        
# @lc code=end

