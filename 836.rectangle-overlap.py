#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        verts1 = [(x,y) for x in [rec1[0],rec1[2]] for y in [rec1[1], rec1[3]]]
        verts2 = [(x,y) for x in [rec2[0],rec2[2]] for y in [rec2[1], rec2[3]]]
        
        return any(map(is_in_rec2, verts))
# @lc code=end

