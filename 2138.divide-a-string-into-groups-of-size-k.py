#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        lst = list(s)
        curr = ''
        while lst:
            curr += lst.pop(0)
            if len(curr) == k:
                result.append(curr)
                curr = ''
        if curr:
            curr += (k-len(curr))*fill
            result.append(curr)
        return result
# @lc code=end

