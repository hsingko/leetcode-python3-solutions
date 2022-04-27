#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        res = [None]*n
        adj = [[] for _ in range(n)]
        visited = set()
        for i,j in pairs:
            adj[i].append(j)
            adj[j].append(i)

        for i in range(n):
            if i in visited:
                continue
            stack = [i]
            chars = []
            idx = []
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                idx.append(curr)
                chars.append(s[curr])
                visited.add(curr)
                stack += adj[curr]
            chars.sort()
            idx.sort()
            for i,v in zip(idx, chars):
                res[i] = v
        return ''.join(res)




# @lc code=end

