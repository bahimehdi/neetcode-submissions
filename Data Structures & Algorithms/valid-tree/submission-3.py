class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        
        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                elif neighbor in visited:
                    return False

                elif dfs(neighbor, node) == False:
                    return False
                
            return True

        if dfs(0, None) == False:
            return False

        if len(visited) < n:
            return False
        return True