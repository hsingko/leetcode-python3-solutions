#
# @lc app=leetcode id=2164 lang=python3
#
# [2164] Sort Even and Odd Indices Independently
#

# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # even
        for i in range(n-2 if n%2==0 else n-1, -1, -2):
            for j in range(0,i,2):
                if nums[j] > nums[j+2]:
                    nums[j], nums[j+2] = nums[j+2], nums[j]
        # odd
        for i in range(n-1 if n%2==0 else n-2, 0, -2):
            for j in range(1, i, 2):
                if nums[j] < nums[j+2]:
                    nums[j], nums[j+2] = nums[j+2], nums[j]
        return nums
# @lc code=end

