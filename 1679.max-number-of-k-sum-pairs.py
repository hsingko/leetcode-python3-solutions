#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        left = 0
        right = n - 1
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                res += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return res
# @lc code=end

