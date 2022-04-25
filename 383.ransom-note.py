#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_count = Counter(magazine)
        r_count = Counter(ransomNote)
        for c in r_count:
            if c not in m_count or m_count[c] < r_count[c]:
                return False
        return True
# @lc code=end

