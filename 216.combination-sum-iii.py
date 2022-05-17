#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k or n > k*9:
            return []
        result = []

        def backtrack(n, k, pos, curr):
            if k < 0 or n < 0:
                return
            if n == 0 and k == 0: 
                result.append(list(curr))
                return
            for i in range(pos+1, 10):
                backtrack(n-i, k-1, i, curr+[i])
        backtrack(n, k, 0, [])
        return result

class Solution1:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k or n > k*9:
            return [[]]
        result = []

        def backtrack(n, k, pos, curr):
            if k < 0 or n < 0:
                return
            if n == 0 and k == 0:
                result.append(list(curr))
                return
            # what's the problem of this code?
            for i in range(pos+1, 10):
                backtrack(n-pos, k-1, i, curr+[pos])
        backtrack(n, k, 1, [])
        return result
# @lc code=end

