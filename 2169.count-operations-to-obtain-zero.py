#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while min(num1, num2) > 0:
            if num1 > num2:
                num1 = num1-num2
            else:
                num2 = num2 - num1
            ans += 1
        return ans
# @lc code=end

