from functools import cache


class Solution:
    @cache
    def three(self, count):
        if count == 1:
            return 1
        if count == 2:
            return 2
        if count == 3:
            return 4
        return self.three(count - 1) + self.three(count - 2) + self.three(count - 3)

    @cache
    def four(self, count):
        if count == 1:
            return 1
        if count == 2:
            return 2
        if count == 3:
            return 4
        if count == 4:
            return 8
        return (
            self.four(count - 1)
            + self.four(count - 2)
            + self.four(count - 3)
            + self.four(count - 4)
        )

    def countTexts(self, pressedKeys: str) -> int:
        ans = 1
        s = pressedKeys
        n = len(s)
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            curr = j - i
            print(curr)
            if s[i] in "79":
                ans *= self.four(curr)
            else:
                ans *= self.three(curr)
            if ans > 10**9 + 7:
                ans = ans % (10**9 + 7)
            i = j
        return ans


Solution().countTexts("22233")
