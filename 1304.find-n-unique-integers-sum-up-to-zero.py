#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        while n:
            if n == 1:
                ans.append(0)
                n -= 1
            else:
                ans += [n, -n]
                n -= 2
        return ans

# @lc code=end

