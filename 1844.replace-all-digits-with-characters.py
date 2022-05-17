#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1,len(s),2):
            s[i] = chr(ord(s[i-1])+int(s[i]))
        return ''.join(s)

        
# @lc code=end

