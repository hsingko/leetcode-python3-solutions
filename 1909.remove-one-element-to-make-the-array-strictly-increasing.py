#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        pin = 1
        def check(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True
        while pin < n:
            if nums[pin] <= nums[pin-1]:
                if not check(nums[pin+1:]):
                    return False
                if pin-2>=0 and pin+1<n and nums[pin-2] >= nums[pin+1]:
                    return False
                # delete a
                if (pin-2<0 or nums[pin]>nums[pin-2]) and (pin+1>=n or nums[pin]<nums[pin+1]):
                    return True
                # delete b
                if (pin-2<0 or nums[pin-1]>nums[pin-2]) and (pin+1>=n or nums[pin-1]<nums[pin+1]):
                    return True
                return False
            pin += 1
        return True

# @lc code=end

