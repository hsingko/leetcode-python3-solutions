#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for key in rooms[curr]:
                stack.append(key)
        return len(visited) == len(rooms)
# @lc code=end

