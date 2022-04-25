class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        v = start ^ goal
        while v:
            ans += v & 1
            v = v >> 1
        return ans
