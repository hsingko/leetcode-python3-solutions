#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evens = []
        odds = []
        while nums:
            curr = nums.pop(0)
            if curr % 2 == 0:
                evens.append(curr)
            else:
                odds.append(curr)
        return evens + odds
        
# @lc code=end

