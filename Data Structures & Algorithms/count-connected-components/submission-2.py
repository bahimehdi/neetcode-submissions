class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()

        graph = {a: [] for a in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            nonlocal count
            visited.add(node)

            for child in graph[node]:
                if child in visited:
                    continue
                dfs(child)
        
        for node in graph:
            if node in visited:
                continue
            count += 1
            dfs(node)
            
        return count