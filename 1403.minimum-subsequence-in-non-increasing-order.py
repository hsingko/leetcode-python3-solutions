#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        result = []
        acc = 0
        for num in nums:
            acc += num
            result.append(num)
            if acc*2 > total:
                return result
        return result
# @lc code=end

