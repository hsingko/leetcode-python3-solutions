#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def backtrack(idx, curr):
            if idx >= n:
                result.append(list(curr))
                return
            for i in range(idx+1, n+1):
                if is_palindrome(s[idx:i]):
                    backtrack(i, curr+[s[idx:i]])
        backtrack(0, [])
        return result
            
# @lc code=end

