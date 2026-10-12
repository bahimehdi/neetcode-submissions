class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        path = set()
        visited = set()
        
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

            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True