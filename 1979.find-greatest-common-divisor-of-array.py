#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a%b == 0:
                return b
            return gcd(b, a%b)
        return gcd(max(nums), min(nums))

# @lc code=end

