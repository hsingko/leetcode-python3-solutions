#
# @lc app=leetcode id=2027 lang=python3
#
# [2027] Minimum Moves to Convert String
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        curr = 0
        while curr < len(s):
            if s[curr] == 'X':
                ans += 1
                curr += 3
            else:
                curr += 1
        return ans
# @lc code=end

