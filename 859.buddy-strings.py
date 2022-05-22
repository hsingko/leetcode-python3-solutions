#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n!=len(goal):
            return False
        if s == goal:
            if max(Counter(s).values()) > 1:
                return True
            return False
        count = 0
        diff = []
        for i in range(n):
            if s[i] != goal[i]:
                if count > 2:
                    return False
                count += 1
                diff.append(i)
        return count == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
# @lc code=end

