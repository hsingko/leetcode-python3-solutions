#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter = Counter(''.join(words))
        for _,t in counter.items():
            if t%n != 0:
                return False
        return True
# @lc code=end

