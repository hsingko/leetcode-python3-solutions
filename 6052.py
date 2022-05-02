class Solution:
    def minimumAverageDifference(self, nums) -> int:
        ans = -1
        right = sum(nums)
        n = len(nums)
        minDiff = float('inf')
        left = 0
        for i in range(n):
            left += nums[i]
            right -= nums[i]
            diff = abs(left//(i+1)-(right//(n-i-1) if i<n-1 else 0))
            print(diff)
            if diff < minDiff:
                minDiff = diff
                ans = i
        return ans

Solution().minimumAverageDifference([1,2,3,4,5])