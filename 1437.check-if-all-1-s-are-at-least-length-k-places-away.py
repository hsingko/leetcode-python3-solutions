#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        occ = []
        for i, v in enumerate(nums):
            if v == 1:
                occ.append(i)
        if len(occ) < 2:
            return True
        return min(map(lambda x:x[0]-x[1]-1, zip(occ[1:], occ))) >= k
# @lc code=end

