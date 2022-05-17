#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m*n != len(original):
            return result
        count = 0
        row = []
        while original:
            row.append(original.pop(0))
            count += 1
            if count == n:
                count = 0
                result.append(row)
                row = []
        return result



# @lc code=end

