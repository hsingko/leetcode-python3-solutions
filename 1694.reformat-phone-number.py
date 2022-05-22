#
# @lc app=leetcode id=1694 lang=python3
#
# [1694] Reformat Phone Number
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        strip = number.replace(' ', '').replace('-', '')
        result = ''
        while strip:
            length = len(strip)
            if length > 4:
                result += strip[:3]
                result += '-'
                strip = strip[3:]
            elif length == 4:
                result += strip[:2]
                result += '-'
                result += strip[2:]
                break
            else:
                result += strip
                break
        return result
# @lc code=end

