#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        result = []
        for word, occ in c1.items():
            if word not in c2 and occ == 1:
                result.append(word)
        for word, occ in c2.items():
            if word not in c1 and occ == 1:
                result.append(word)
        return result

# @lc code=end

