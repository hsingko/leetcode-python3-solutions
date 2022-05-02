#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                op1 = stack.pop()
                op2 = stack.pop()
                if token == '+':
                    stack.append(op1+op2)
                elif token == '-':
                    stack.append(op2-op1)
                elif token == '*':
                    stack.append(op2*op1)
                else:
                    stack.append(int(op2/op1))
            else:
                stack.append(int(token))
        return stack.pop()
# @lc code=end

