from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1

        queue = [
            course for course, indegree in enumerate(indegrees) if indegree == 0
        ]
        head = 0
        completed = 0

        while head < len(queue):
            course = queue[head]
            head += 1
            completed += 1

            for next_course in graph[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
