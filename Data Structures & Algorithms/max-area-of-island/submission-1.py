class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):
            if (row, col) in visited or row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
                return 0

            visited.add((row, col))

            if grid[row][col] == 0:
                return 0
            
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = max(area, dfs(i, j))

        return area