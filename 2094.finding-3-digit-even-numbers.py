#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []

        # fill 3rd 
        for x in count:
            if x%2==0:
                count[x] -= 1
                # fill 2th
                for y in count:
                    if count[y] > 0:
                        count[y] -= 1
                        # fill 1st
                        for z in count:
                            if count[z] > 0 and z>0:
                                result.append(z*100+y*10+x)
                        count[y] += 1
                count[x]+=1
        return sorted(result)
        
# @lc code=end

