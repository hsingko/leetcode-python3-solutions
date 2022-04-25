#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        arr1 = []
        arr2 = []
        for ch in s:
            if '0' <= ch <='9':
                arr1.append(ch)
            else:
                arr2.append(ch)
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        if len(arr1) - len(arr2) > 1:
            return ""
        result = ""
        while arr1:
            result += arr1.pop()
            if arr2:
                result += arr2.pop()
        return result

# @lc code=end

