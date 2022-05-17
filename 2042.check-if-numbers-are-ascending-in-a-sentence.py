#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = None
        n = len(s)
        i = 0
        while i < n:
            if '0'<=s[i]<='9':
                j = i
                while j < n and '0'<=s[j]<='9':
                    j += 1
                curr = int(s[i:j])
                i = j
                if not prev:
                    prev = curr
                else:
                    if curr <= prev:
                        return False
                    prev = curr
            else:
                i += 1
        return True


# @lc code=end

