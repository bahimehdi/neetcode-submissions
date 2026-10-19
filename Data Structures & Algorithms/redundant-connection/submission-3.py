from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        rank = [1] * (len(edges)+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
                rank[rootB] += rank[rootA]
            else:
                parent[rootB] = rootA
                rank[rootA] += rank[rootB]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []