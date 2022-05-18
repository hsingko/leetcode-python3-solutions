#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        rows = 1
        width = 0
        for ch in s:
            curr = widths[ord(ch)-ord('a')]
            if width + curr > 100:
                rows += 1
                width = curr
            else:
                width += curr
        return [rows, width]

# @lc code=end

