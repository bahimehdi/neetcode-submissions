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
            board[row][col] = 'S'

            while stack:
                r, c = stack.pop()
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if(
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == 'O'
                    ):
                        board[nr][nc] = 'S'
                        stack.append((nr, nc))

        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][cols - 1] == 'O':
                dfs(row, cols - 1)
            
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[rows - 1][col] == 'O':
                dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'