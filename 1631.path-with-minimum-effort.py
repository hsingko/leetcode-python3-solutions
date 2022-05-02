#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        efforts = defaultdict(lambda: float('inf'))
        m = len(heights)
        n = len(heights[0])
        heap = [(0,0,0)]
        efforts[(0,0)] = 0
        def cal_and_update_min_efforts(x,y,x1,y1):
            efforts[(x1, y1)] = min(efforts[(x1,y1)], max(abs(heights[x][y]-heights[x1][y1]), efforts[(x,y)]))
            return efforts[(x1, y1)]
        while heap:
            _, x, y = heappop(heap)
            if (x, y) in visited:
                continue
            if x > 0:
                v1 = cal_and_update_min_efforts(x,y,x-1,y)
                heappush(heap, (v1, x-1, y))
            if x < m-1:
                v2 = cal_and_update_min_efforts(x,y,x+1,y)
                heappush(heap, (v2, x+1, y))
            if y > 0:
                v3 = cal_and_update_min_efforts(x,y,x,y-1)
                heappush(heap, (v3, x,y-1))
            if y < n-1:
                v4 = cal_and_update_min_efforts(x,y,x,y+1)
                heappush(heap, (v4, x,y+1))
            visited.add((x,y))
        return efforts[(m-1, n-1)]


# @lc code=end

