#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        result = []
        for t in target:
            while curr < t:
                result.append('Push')
                result.append('Pop')
                curr += 1
            result.append('Push')
            curr += 1
        return result

# @lc code=end

