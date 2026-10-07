class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, mesh):
            stack = [(row, col)]
            touchesBorder = False

            while stack:
                r, c = stack.pop()

                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                mesh.add((r, c))

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    touchesBorder = True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and board[nr][nc] == 'O'
                    ):
                        stack.append((nr, nc))
            return touchesBorder
        
        for row in range(rows):
            for col in range(cols):
                if  board[row][col] == 'O' and (row, col) not in visited:
                    mesh = {(row, col)}
                    touchesBorder = dfs(row, col, mesh)
                    if not touchesBorder:
                        for (r, c) in mesh:
                            board[r][c] = 'X'