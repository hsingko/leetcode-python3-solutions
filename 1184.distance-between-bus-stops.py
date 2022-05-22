#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        return min(sum(distance[start:destination]), sum(distance[destination:n]+distance[0:start]))

# @lc code=end

