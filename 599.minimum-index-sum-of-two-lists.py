#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tb1 = {r:i for i, r in enumerate(list1)}
        tb2 = {r:i for i,r in enumerate(list2)}
        result = []
        msum = float('inf')
        for r in tb1:
            if r in tb2:
                curr_sum = tb1[r] + tb2[r]
                if curr_sum < msum:
                    msum = curr_sum
                    result = [r]
                elif curr_sum == msum:
                    result.append(r)
        return result

# @lc code=end

