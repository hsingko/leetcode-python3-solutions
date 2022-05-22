#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, A: List[List[int]]) -> int:
        return sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(x)) for x in A).values())
# @lc code=end

