#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        p1, len1 = 0, len(word1)
        p2, len2 = 0, len(word2)
        while p1<len1 and p2<len2:
            result += word1[p1]
            result += word2[p2]
            p1 += 1
            p2 += 1
        if p1 < len1:
            result += word1[p1:]
        if p2 < len2:
            result += word2[p2:]
        return result
# @lc code=end

