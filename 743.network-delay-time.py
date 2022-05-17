#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        result = -1
        adj = defaultdict(dict)
        for u,v,w in times:
            adj[u][v] = w
        queue = [(0, k)]
        visited = set()
        while queue:
            d, curr = heapq.heappop(queue)
            if curr in visited:
                continue
            result = max(result, d)
            visited.add(curr)
            for node,w in adj[curr].items():
                heapq.heappush(queue, (w+d, node))
        return result if len(visited) == n else -1

        
# @lc code=end

