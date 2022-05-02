#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        v = n^(n>>1)
        while v:
            if v&1 == 0:
                return False
            v >>=1
        return True
# @lc code=end

