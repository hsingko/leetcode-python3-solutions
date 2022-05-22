#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        if total % 2 == 0:
            return total // 2
        elif low % 2 == 0:
            return total // 2
        else:
            return total // 2 + 1
# @lc code=end

