#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class BruteForceSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        def recur(i, s):
            nonlocal count
            if i == n:
                if s == target:
                    count += 1
                return
            recur(i+1, s+nums[i])
            recur(i+1, s-nums[i])
        recur(0, 0)
        return count

class Solution:
    def findTargetSumWays(self, nums, target):
        
# @lc code=end

