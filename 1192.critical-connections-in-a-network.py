#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
from typing import List

class BruteForceSolution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for i in range(n)]
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)

        def is_critical(x, y):
            stack = [x]
            visited = set()
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for v in adj[curr]:
                    if curr == x and v == y:
                        continue
                    stack.append(v)
            return len(visited) != n
        
        result = []
        for x, y in connections:
            if is_critical(x,y):
                result.append([x,y])
        return result
        
# Tarjans algorithm
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        timer = 0
        result = []
        visited = set()
        visit_time = [0]*n
        def dfs(parent, node):
            nonlocal timer
            visited.add(node)
            visit_time[node] = now =timer
            timer += 1
            for neig in adj[node]:
                if neig == parent:
                    continue
                if neig not in visited:
                    dfs(node, neig)
                visit_time[node] = min(visit_time[node], visit_time[neig])
                if now < visit_time[neig]:
                    result.append([node, neig])
        dfs(-1, 0)
        return result
            
 
# @lc code=end

