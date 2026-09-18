# size of string = 2n
# The base case -> len(string) == 2n
# Choices -> add '(', add ')'
# Constraints -> never use more than 'n' of each type of parenthesis ==> use open and close variables to store the count. And if at any time close > open, we stop the currrent leaf
# Backtracking step -> pop the last parenthesis added

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(string, openCount, closeCount):
            if closeCount > openCount or closeCount > n or openCount > n:
                return

            if len(string) == 2 * n and openCount == closeCount:
                res.append(string[:])
                return

            if openCount < n:
                backtrack(string + '(', openCount + 1, closeCount)
            
            if closeCount < openCount:
                backtrack(string + ')', openCount, closeCount + 1)

        backtrack("", 0, 0)
        return res