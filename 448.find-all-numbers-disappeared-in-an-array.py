#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tb = [0]*(n+1)
        for num in nums:
            tb[num] = 1
        ans = []
        for idx, val in enumerate(tb):
            if val == 0 and idx>0:
                ans.append(idx)
        return ans
# @lc code=end

