#
# @lc app=leetcode id=2062 lang=python3
#
# [2062] Count Vowel Substrings of a String
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        left = 0
        n = len(word)
        while left < n:
            if word[left] not in 'aeiou':
                left += 1
                continue
            tb = defaultdict(int)
            right = left
            while right < n and word[right] in 'aeiou':
                tb[word[right]] += 1
                if len(tb) == 5:
                    ans += 1
                right += 1
            while left < right:
                left += 1
                tb[word[left]] -= 1
                if tb[word[left]] == 0:
                    del tb[word[left]]
                    break
                ans += 1
            left = right
            
        return ans


# @lc code=end

