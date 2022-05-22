#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        canType = 0
        words = text.split()
        broken = set(brokenLetters)
        for word in words:
            if not set(word).intersection(broken):
                canType += 1
        return canType

# @lc code=end

