#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = {i for i in range(n)}
        for _, j in edges:
            if j in nodes:
                nodes.remove(j)
        return list(nodes)
# @lc code=end

