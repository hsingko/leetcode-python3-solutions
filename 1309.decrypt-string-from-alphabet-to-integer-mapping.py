#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        d = dict(zip([str(i) for i in range(1,27)], list('abcdefghijklmnopqrstuvwxyz')))
        n = len(s)
        p = 0
        while p < n:
            if p < n-2 and s[p+2] == '#':
                res += d[s[p:p+2]]
                p += 3
            else:
                res += d[s[p]]
                p += 1
        return res            
        
# @lc code=end

