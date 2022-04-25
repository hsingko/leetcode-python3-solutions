class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)
        n = len(s)
        for i in range(0, n, 2 * k):
            left = i
            right = min(i + k - 1, n - 1)
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        return "".join(lst)
