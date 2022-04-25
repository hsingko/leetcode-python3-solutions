#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(digit):
            ans = 0
            while digit > 0:
                ans += digit%10
                digit //= 10
            return ans

        count = 0
        for i in range(1, num+1):
            if digit_sum(i) % 2 == 0:
                count += 1
        return count
        
# @lc code=end

