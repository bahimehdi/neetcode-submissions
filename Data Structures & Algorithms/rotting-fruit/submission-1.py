from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        freshCount = 0
        rottenFruits = deque()

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshCount += 1
                if grid[row][col] == 2:
                    rottenFruits.append((row, col))

        if freshCount == 0:
            return minutes

        def bfs():
            nonlocal freshCount, minutes
            currentRottenCount = len(rottenFruits)
            i = 0

            while i != currentRottenCount:
                node = rottenFruits.popleft()

                if node[0] > 0 and grid[node[0] - 1][node[1]] == 1:
                    grid[node[0] - 1][node[1]] = 2
                    freshCount -= 1
                    rottenFruits.append((node[0] - 1, node[1]))
                if node[0] < rows - 1 and grid[node[0] + 1][node[1]] == 1:
                    grid[node[0] + 1][node[1]] = 2
                    freshCount -= 1
                    rottenFruits.append((node[0] + 1, node[1]))
                if node[1] > 0 and grid[node[0]][node[1] - 1] == 1:
                    grid[node[0]][node[1] - 1] = 2
                    freshCount -= 1
                    rottenFruits.append((node[0], node[1] - 1))
                if node[1] < cols - 1 and grid[node[0]][node[1] + 1] == 1:
                    grid[node[0]][node[1] + 1] = 2
                    freshCount -= 1
                    rottenFruits.append((node[0], node[1] + 1))
                i += 1

            minutes += 1

        while rottenFruits and freshCount != 0:
            bfs()

        if freshCount > 0:
            return -1
        return minutes