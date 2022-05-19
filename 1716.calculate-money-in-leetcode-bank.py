#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        money = 0
        for i in range(n):
            if i > 0 and i%7 == 0:
                money -= 5
            else:
                money += 1
            ans += money
        return ans
# @lc code=end

