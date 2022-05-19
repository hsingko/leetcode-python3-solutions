#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        squares = set([i*i for i in range(1,n+1)])
        for i in range(1, n+1):
            for j in range(1, n+1):
                t = i**2 + j**2
                if t in squares:
                    ans += 1
        return ans
# @lc code=end

