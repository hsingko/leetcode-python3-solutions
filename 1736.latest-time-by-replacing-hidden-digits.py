#
# @lc app=leetcode id=1736 lang=python3
#
# [1736] Latest Time by Replacing Hidden Digits
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        s = list(time)
        for idx, val in enumerate(time):
            if val == '?':
                if idx == 0:
                    s[idx] = '2'
                elif idx == 1:
                    if s[idx-1] == '2':
                        s[idx] = '4'
                    
# @lc code=end

