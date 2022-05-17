#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        def dfs(pos, curr):
            nonlocal result
            if pos == n:
                result += curr
                return
            dfs(pos+1, curr)
            dfs(pos+1, curr^nums[pos])
        dfs(0, 0)
        return result
# @lc code=end

