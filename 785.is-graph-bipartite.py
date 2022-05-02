#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class UglySolution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = set()
        stack = []
        while len(visited) < n:
            if not stack:
                A = set()
                B = set()
                for i in range(n):
                    if i not in visited:
                        stack = [i]
                        A.add(i)
                        break
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                belong = A if curr in A else B
                other = B if curr not in B else A
                for adj in graph[curr]:
                    if adj in belong:
                        return False
                    other.add(adj)
                    stack.append(adj)
        
        return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, colored = len(graph), {}
        def dfs_color(color, idx, colored):
            if idx in colored:
                return colored[idx] == color
            colored[idx] = color
            return all(dfs_color(-color, neig, colored) for neig in graph[idx])
        return all(i in colored or dfs_color(1, i, colored) for i in range(n))

# @lc code=end

