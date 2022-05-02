#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = 1
        while n > x:
            x = x*2+1
        return x - n
# @lc code=end

