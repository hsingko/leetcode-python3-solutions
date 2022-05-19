#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        tb = dict(zip('abcdefghij', '0123456789'))
        def get_num(s):
            res = ''
            for ch in s:
                res += tb[ch]
            return int(res)
        return get_num(firstWord) + get_num(secondWord) == get_num(targetWord)
# @lc code=end

