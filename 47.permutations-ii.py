#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        group = Counter(nums)
        results = []
        n = len(nums)

        def dfs(result, group):
            if len(result) == n:
                results.append(result)
                return
            for num in group:
                if group[num] > 0:
                    group[num] -= 1
                    dfs(result+[num], group)
                    group[num] += 1
        dfs([], group)
        return results
# @lc code=end

