class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        path = set()
        visited = set()
        order = []
        
        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)

            for child in graph[node]:
                if dfs(child) == False:
                    return False
            
            path.remove(node)
            visited.add(node)
            order.append(node)

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return order[::-1]