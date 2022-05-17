#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left = 0
        n = len(nums)
        right = n-1
        while left < n and sorted_nums[left] == nums[left]:
            left += 1
        while right > -1 and sorted_nums[right] == nums[right]:
            right -= 1
        return right - left + 1 if left <= right else 0
# @lc code=end

