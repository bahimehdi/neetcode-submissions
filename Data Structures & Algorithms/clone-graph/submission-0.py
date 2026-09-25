"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
            
        visited = {}
        
        def dfs(node):
            if node not in visited:
                visited[node] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
                visited[node].neighbors.append(visited[neighbor])
            
            return visited[node]
            
        dfs(node)
        
        return visited[node]