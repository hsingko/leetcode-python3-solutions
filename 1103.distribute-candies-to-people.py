#
# @lc app=leetcode id=1103 lang=python3
#
# [1103] Distribute Candies to People
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        result = [0]*n
        curr = 0
        give = 1
        while candies>0:
            result[curr] += min(give, candies)
            candies -= give
            give += 1
            curr += 1
            if curr == n:
                curr = 0
        return result
        
# @lc code=end

