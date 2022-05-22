#
# @lc app=leetcode id=1995 lang=python3
#
# [1995] Count Special Quadruplets
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ans += 1
        return ans

# @lc code=end

