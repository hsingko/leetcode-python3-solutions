#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 !=0:
            return False
        each = total // 3
        curr = 0
        count = 0
        while arr:
            curr += arr.pop()
            if curr == each:
                curr = 0
                count += 1
                if count == 2 and arr:
                    return True
        return False
# @lc code=end

