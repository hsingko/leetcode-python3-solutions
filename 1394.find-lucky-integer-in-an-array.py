#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for v, t in Counter(arr).items():
            if v == t:
                res = max(res, v)
        return res
# @lc code=end

