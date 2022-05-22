#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        def extend(left, right):
            nonlocal ans,n
            while left > -1 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        for i in range(len(s)):
            extend(i, i)
            extend(i,i+1)
        return ans
# @lc code=end

