# base case: if len(positions) == 4  => append to res (if we reach len(positions) to 4, it's for sure a valid one)
# state: position of placed queens, what queen to place next
# choices: possible position for current queen
# constraints: new positions mustn't be attacked
# backtracking step: add position, recurse, remove position
# eg: n=4 -> 4x4 -> 4-queens -> queen 1 starts at any position, next queen starts at any position that respects queen 1 position,.. seemingly factorial complexity
# i think the state is the current psoitions takes, if a new queen can't take any position, we return

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(positions):
            col = len(positions)

            if col == n:
                board = [["."] * n for _ in range(n)]

                for queenCol, queenRow in enumerate(positions):
                    board[queenRow][queenCol] = "Q"

                res.append(["".join(row) for row in board])

            for row in range(n):
                valid = True

                for prevCol, prevRow in enumerate(positions):
                    if row == prevRow:
                        valid = False
                        break
                    
                    if row - col == prevRow - prevCol:
                        valid = False
                        break
                    
                    if row + col == prevRow + prevCol:
                        valid = False
                        break
                    
                if not valid:
                    continue

                positions.append(row)
                backtrack(positions)
                positions.pop()

        backtrack([])
        return res