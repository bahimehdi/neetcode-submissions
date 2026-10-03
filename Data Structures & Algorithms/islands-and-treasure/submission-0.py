from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        queue = deque()

        def bfs():
            while queue:
                node = queue.popleft()

                neighbors = []
                if node[0] > 0:
                    neighbors.append((node[0] - 1, node[1]))
                if node[0] < len(grid) - 1:
                    neighbors.append((node[0] + 1, node[1]))
                if node[1] > 0:
                    neighbors.append((node[0], node[1] - 1))
                if node[1] < len(grid[0]) - 1:
                    neighbors.append((node[0], node[1] + 1))

                for neighbor in neighbors:
                    if grid[neighbor[0]][neighbor[1]] == INF:
                        grid[neighbor[0]][neighbor[1]] = grid[node[0]][node[1]] + 1
                        queue.append(neighbor)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        bfs()