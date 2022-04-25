#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        candidates =[0]*101
        res = []
        exclude = {0,1,2,4}
        for num in nums1:
            candidates[num] |= 1
        for num in nums2:
            candidates[num] |= 2
        for num in nums3:
            candidates[num] |= 4
        for idx, can in enumerate(candidates):
            if can not in exclude:
                res.append(idx)
        return res
# @lc code=end

