#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        stack = [source]
        visited = set()
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            if curr == destination:
                return True
            visited.add(curr)
            for neig in adj[curr]:
                stack.append(neig)
        return False
# @lc code=end

