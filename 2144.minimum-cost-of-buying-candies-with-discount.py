#
# @lc app=leetcode id=2144 lang=python3
#
# [2144] Minimum Cost of Buying Candies With Discount
#

# @lc code=start
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        count = 0
        while cost:
            if count == 2:
                cost.pop()
                count = 0
            else:
                ans += cost.pop()
                count += 1
        return ans
            

# @lc code=end

