#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for s in score:
            heapq.heappush(heap, -s)
        tb = {}
        curr = 1
        while heap:
            s = -heapq.heappop(heap)
            if curr == 1:
                tb[s] = 'Gold Medal'
            elif curr == 2:
                tb[s] = 'Silver Medal'
            elif curr == 3:
                tb[s] = 'Bronze Medal'
            else:
                tb[s] = str(curr)
            curr += 1
        return [tb[i] for i in score]

# @lc code=end

