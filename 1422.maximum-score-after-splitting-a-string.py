#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        ans = 0
        for divide in range(0, len(s)-1):
            if s[divide] == '0':
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, ones+zeros)
        return ans
# @lc code=end

