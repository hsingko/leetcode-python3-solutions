#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class SolutionWithN2:
    def find132pattern(self, nums: List[int]) -> bool:
        mininal = nums[0]
        for i in range(1, len(nums)-1):
            mininal = min(mininal, nums[i])
            if mininal == nums[i]:
                continue
            for j in range(i+1, len(nums)):
                if mininal < nums[j] < nums[i]:
                    return True
        return False

# mono-stack solution
class Solution:
    def find132pattern(self, nums):
        stack = []
        minLeft = nums[0]
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num, minLeft))
            minLeft = min(minLeft, num)
        return False
# @lc code=end

