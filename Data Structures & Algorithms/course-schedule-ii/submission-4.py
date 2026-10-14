from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
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
        
        return order if len(order) == numCourses else []