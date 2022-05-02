#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask1 = 1<<7
        mask2 = 1<<6
        bytes = 0
        for num in data:
            mask = 1<<7
            if bytes == 0:
                while mask & num:
                    bytes += 1
                    mask >>=1
                if bytes == 0:
                    continue
                if bytes == 1 or bytes > 4:
                    return False
            else:
                if not(num&mask1 and not (num&mask2)):
                    return False
            bytes -= 1
        return bytes == 0
# @lc code=end

