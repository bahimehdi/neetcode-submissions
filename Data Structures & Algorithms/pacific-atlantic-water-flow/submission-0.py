class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visited = set()
        pacificFlow = set()
        atlanticFlow = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, visited):
            visited.add((row, col))
            neighbors = set()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if(
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[row][col]
                ):
                    dfs(nr, nc, visited)

        for row in range(rows):
            dfs(row, 0, pacificFlow)
            dfs(row, cols - 1, atlanticFlow)

        for col in range(cols):
            dfs(0, col, pacificFlow)
            dfs(rows - 1, col, atlanticFlow)
        
        return [list(cell) for cell in pacificFlow & atlanticFlow]