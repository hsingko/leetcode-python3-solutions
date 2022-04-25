#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        prev = points[0]
        for point in points[1:]:
            ans += max(abs(point[0]-prev[0]), abs(point[1]-prev[1]))
            prev = point
        return ans
# @lc code=end

