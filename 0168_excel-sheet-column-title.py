class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        def name(idx):
            return chr(ord("A") + idx - 1)

        while columnNumber:
            curr = columnNumber % 26
            if curr == 0:
                curr = 26
            ans = name(curr) + ans
            columnNumber = (columnNumber - curr) // 26
        return ans
