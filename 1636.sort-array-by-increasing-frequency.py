#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = list(Counter(nums).items())
        c.sort(key=lambda x:(x[1], -x[0]))
        result = []
        for val,count in c:
            for _ in range(count):
                result.append(val)
        return result

# @lc code=end

