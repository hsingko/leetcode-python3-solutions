#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr1 = sorted(ransomNote)
        arr2 = sorted(magazine)
        while arr2:
            if not arr1:
                return True
            if arr1[0] == arr2[0]:
                arr1.pop(0)
                arr2.pop(0)
            elif arr1[0] < arr2[0]:
                return False
            else:
                arr2.pop(0)
        return not arr1
# @lc code=end

