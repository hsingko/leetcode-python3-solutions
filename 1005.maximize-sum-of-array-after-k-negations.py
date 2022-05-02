#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i<n and nums[i] < 0 and k:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k == 0 or k%2==0:
            return sum(nums)
        return sum(nums) - 2*min(nums)

# @lc code=end

