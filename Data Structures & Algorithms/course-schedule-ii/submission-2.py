from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        indegree = {course: 0 for course in range(numCourses)}

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in indegree:
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for child in graph[node]:
                indegree[child] -= 1

                if indegree[child] == 0:
                    queue.append(child)
        
        if len(order) == numCourses:
            return order
        else:
            return []