#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        string = list(str(num))
        n = len(string)
        for i in range(n-1):
            max_swap = -1
            for j in range(i+1, n):
                if string[j] > string[i]:
                    if max_swap < 0 or string[j] >= string[max_swap]:
                        max_swap = j
            if max_swap > 0:
                string[i], string[max_swap] = string[max_swap], string[i]
                break
        return int(''.join(string))


# @lc code=end

