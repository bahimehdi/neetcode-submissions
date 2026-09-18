# The base case -> k == len(word) => exists = True
# Choices -> add prior (row-1), add next(row+1), add upper(col+1), add lower(col-1)
# Constraints -> cell outside of the board OR board[row][col] != word[k] OR cell already in current path
# Backtracking step -> if invalid or visited, return, if not backtrack the choices

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False
        visited = set()

        def backtrack(row, col, k):
            nonlocal exists
            if k == len(word):
                exists = True
                return

            if (row, col) in visited or board[row][col] != word[k]:
                return
            else:
                if k == len(word) - 1:
                    exists = True
                    return
                visited.add((row, col))
                if row < len(board) - 1:
                    backtrack(row+1, col, k+1)
                if row > 0:
                    backtrack(row-1, col, k+1)
                if col < len(board[0]) - 1:
                    backtrack(row, col+1, k+1)
                if col > 0:
                    backtrack(row, col-1, k+1)
                visited.remove((row, col))

        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r, c, 0)
        return exists