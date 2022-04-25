#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def cap(word: str):
            if len(word) < 3:
                return word.lower()
            return word.capitalize()
        return ' '.join(map(cap, title.split()))
# @lc code=end

