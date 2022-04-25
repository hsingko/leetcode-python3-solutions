#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        flag = False
        for c in count:
            times = count[c]
            if times % 2 == 0:
                ans += times
            elif not flag:
                ans += times
                flag = True
            else:
                ans += (times-1)
        return ans

        
# @lc code=end

