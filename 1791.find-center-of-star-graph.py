#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        ec = [0]*(n+1)
        for i, j in edges:
            ec[i] += 1
            ec[j] += 1
            if ec[i] == n-1:
                return i
            if ec[j] == n-1:
                return j
        return -1
# @lc code=end

