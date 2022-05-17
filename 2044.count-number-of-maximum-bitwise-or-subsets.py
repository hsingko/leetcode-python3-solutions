#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum, count = 0, 0
        n = len(nums)

        def dfs(idx, curr):
            nonlocal maximum, count
            if idx == n:
                if curr == maximum:
                    count += 1
                elif curr > maximum:
                    maximum = curr
                    count = 1
                return
            dfs(idx+1, curr|nums[idx])
            dfs(idx+1, curr)
        dfs(0, 0)
        return count
# @lc code=end

