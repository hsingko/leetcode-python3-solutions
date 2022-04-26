#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j in range(n-1, i, -1):
                    arr[j] = arr[j-1]
                i += 2
            else:
                i += 1
        

                
        
# @lc code=end

