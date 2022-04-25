class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.count = n

    def connect(self, i, j):
        parent = self.parent
        pi, pj = parent(i), parent(j)
        if pi == pj:
            return
        self.count -= 1
        self.p[pj] = pi

    def parent(self, i):
        p = self.p
        while p[i] != i:
            i = p[i]
        return i

    def count(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.connect(i, j)
        return uf.count
