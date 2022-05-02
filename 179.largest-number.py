#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class LargerNumKey(str):
            def __lt__(x, y) -> bool:
                return x+y > y+x
        ans = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if ans[0] == '0' else ans
# @lc code=end

