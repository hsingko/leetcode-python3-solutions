#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        has_words = False
        for ch in s:
            if ch == ' ' and has_words:
                ans += 1
                has_words = False
            elif ch != ' ':
                has_words = True
        if has_words:
            ans += 1
        return ans
        
# @lc code=end

