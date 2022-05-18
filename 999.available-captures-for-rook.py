#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    # look left
                    for y in range(j-1, -1, -1):
                        if board[i][y] == 'B':
                            break
                        elif board[i][y] == 'p':
                            ans += 1
                            break
                    # look right
                    for y in range(j+1, 8):
                        if board[i][y] == 'B':
                            break
                        elif board[i][y] == 'p':
                            ans += 1
                            break
                    # look up
                    for x in range(i-1, -1, -1):
                        if board[x][j] == 'B':
                            break
                        elif board[x][j] == 'p':
                            ans += 1
                            break
                    # look right
                    for x in range(i+1, 8):
                        if board[x][j] == 'B':
                            break
                        elif board[x][j] == 'p':
                            ans += 1
                            break
        return ans
# @lc code=end

