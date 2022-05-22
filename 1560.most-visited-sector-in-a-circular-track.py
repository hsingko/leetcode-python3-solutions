#
# @lc app=leetcode id=1560 lang=python3
#
# [1560] Most Visited Sector in  a Circular Track
#

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = {i:0 for i in range(1,n+1)}
        for i, j in zip(rounds, rounds[1:]):
            if i < j:
                for k in range(i,j+1):
                    visited[k] += 1
            else:
                for k in range(i, n+1):
                    visited[k] += 1
                for k in range(1,i):
                    visited[k] += 1
        result = []
        max_times = 0
        for i, t in visited.items():
            if t > max_times:
                result = [i]
                max_times = t
            elif t == max_times:
                result.append(i)
        return result

# @lc code=end

