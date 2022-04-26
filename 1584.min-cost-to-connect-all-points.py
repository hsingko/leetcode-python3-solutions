#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        mset = set()
        minheap = [(0, 0)] # (distance, point)
        def distance(i, j):
            pi = points[i]
            pj = points[j]
            return abs(pi[0]-pj[0]) + abs(pi[1]-pj[1])
        while len(mset) < n:
            dis, curr = heappop(minheap)
            if curr in mset:
                continue
            ans += dis
            mset.add(curr)
            for i in range(n):
                if i not in mset:
                    heappush(minheap, (distance(i, curr), i))
        return ans
            

# @lc code=end

