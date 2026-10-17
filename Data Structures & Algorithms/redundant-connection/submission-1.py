class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(curr, target):
            if curr == target:
                return True
            
            visited.add(curr)
            for child in graph[curr]:
                if child in visited:
                    continue
                if child == target:
                    return True
                if dfs(child, target):
                    return True
            return False

        for a, b in edges:
            visited = set()
            if dfs(a, b) == True:
                return [a, b]
            else:
                graph[a].append(b)
                graph[b].append(a)