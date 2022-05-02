#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def get_factors(num):
            res = []
            for i in range(1,num):
                if num%i == 0:
                    res.append(i)
            return res
        
        @cache
        def step(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return step(num//2) + 2
            factors = get_factors(num)
            if not factors:
                return num
            return min([step(fac)+num//fac for fac in factors])
        return step(n)
            
# @lc code=end

