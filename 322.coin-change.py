#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        tb = set(coins)
        @cache
        def change(amount):
            if amount == 0:
                return 0
            if amount in tb:
                return 1
            ans = -1
            for coin in coins:
                if coin < amount:
                    res = change(amount-coin)
                    if res > -1 and (ans == -1 or res < ans):
                        ans = res 
            if ans == -1:
                return -1
            else:
                return ans+1
        return change(amount)            
            
# @lc code=end

