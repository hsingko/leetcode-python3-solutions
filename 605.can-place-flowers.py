#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for i in range(size):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i < size-1 and flowerbed[i+1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
        return n == 0
# @lc code=end

