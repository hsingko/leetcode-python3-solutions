#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        lst = list(s)
        while lst and lst[-1] == 'b':
            lst.pop()
        return 'b' not in lst
# @lc code=end

