class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()

                board[r][c] = 'S'
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if(
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == 'O'
                    ):
                        stack.append((nr, nc))



        for row in range(rows):
            for col in range(cols):
                if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and board[row][col] == 'O':
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'