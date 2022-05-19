#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
from collections import Counter
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        values = list(counter.values())
        def gcd(a, b):
            if a > b:
                return gcd(b, a)
            if b%a == 0:
                return a
            return gcd(b%a, a)
        return reduce(gcd, values) > 1
# @lc code=end

