#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
from re import sub


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ''
        tb = set(s)
        for idx, ch in enumerate(s):
            if ch.lower() in tb and ch.upper() in tb:
                continue
            sub1 = self.longestNiceSubstring(s[:idx])
            sub2 = self.longestNiceSubstring(s[idx+1:])
            if len(sub1) >= len(sub2):
                return sub1
            else:
                return sub2
        return s
# @lc code=end

