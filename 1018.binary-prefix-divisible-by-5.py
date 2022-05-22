#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = 0
        ans = []
        for num in nums:
            curr <<= 1
            curr += num
            if curr % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
# @lc code=end

