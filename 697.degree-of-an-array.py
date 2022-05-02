#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for idx, val in enumerate(nums):
            if val not in left:
                left[val] = idx
            right[val] = idx
            count[val] = count.get(val, 0) + 1
        degree = max(count.values())
        ans = float('inf')
        for key, c in count.items():
            if c == degree:
                ans = min(ans, right[key] - left[key] + 1)
        return ans
# @lc code=end

