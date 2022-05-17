#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#

# @lc code=start
from numpy import double


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 == 1:
            return []
        
        counter = Counter(changed)
        doubled = []

        for num, occurs in counter.items():
            if 2*num not in counter:
                doubled.append([num]*occurs)
            elif 2*num == num:
                if occurs % 2 == 1:
                    return []
                else:
                    doubled.append([num]*(occurs//2))
        if len(doubled)*2 != n:
            return []
        else:
            return list(map(lambda x:x//2, doubled))
# @lc code=end

