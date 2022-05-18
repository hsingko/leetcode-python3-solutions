#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 2:
            return False
        i = 1
        while n > 0:
            n -= i
            i += 2
        return n == 0
# @lc code=end

