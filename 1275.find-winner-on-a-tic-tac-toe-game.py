#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        if n < 9:
            if n%2 == 1:
                return 'A'
            else:
                return 'B'
        else:
            aMoves = [tuple(moves[i]) for i in range(0,9,2)]
            x, y =aMoves[-1]
            if (x,0) in aMoves and (x,1) in aMoves and (x,2) in aMoves:
                return 'A'
            if (0,y) in aMoves and (1,y) in aMoves and (2,y) in aMoves:
                return 'A'
            if x == y and (0,0) in aMoves and (1,1) in aMoves and (2,2) in aMoves:
                return 'A'
            if x+y==2 and (0,2) in aMoves and (1,1) in aMoves and (2,0) in aMoves:
                return 'A'
            return 'Draw'
# @lc code=end

