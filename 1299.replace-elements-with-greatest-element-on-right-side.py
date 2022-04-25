#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr)-1,-1,-1):
            tmp = max(arr[i], greatest)
            arr[i] = greatest
            greatest = tmp
        return arr
# @lc code=end

