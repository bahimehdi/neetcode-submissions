class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(row, col):
            nonlocal islands

            if (row, col) in visited or row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
                return

            visited.add((row, col))

            if grid[row][col] == "0":
                return

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands