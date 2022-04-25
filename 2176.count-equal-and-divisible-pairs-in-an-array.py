#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and i*j%k==0:
                    ans += 1
        return ans

        
# @lc code=end

