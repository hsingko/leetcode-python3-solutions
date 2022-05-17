#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        tb = [0]*10
        for ch in s:
            if '0' <= ch <= '9':
                tb[int(ch)] = 1
        largest = -1
        for idx in range(9, -1, -1):
            if tb[idx] > 0:
                if largest == -1:
                    largest = idx
                else:
                    return idx
        return -1
# @lc code=end

