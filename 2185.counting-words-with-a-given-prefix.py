#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        pl = len(pref)

        for word in words:
            if word[:pl] == pref:
                ans += 1
        return ans
        
# @lc code=end

