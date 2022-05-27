from collections import defaultdict

class Solution:
    def hasCycle(self, course, graph, seen):
        if seen[course]:
            return True

        seen[course] = True

        ret = False
        for neighbours in graph[course]:
            ret = self.hasCycle(neighbours, graph, seen)
            if ret:
                break
        seen[course] = False

        return ret

    def canFinishCourse(self, numCourses, prerequisites):
        # use the graph to solve the problem. As a first step, create the graph dictionary
        graph = defaultdict(list)
        for course1, course2 in prerequisites:
            if course1 in graph:
                graph[course1].append(course2)
            else:
                graph[course1] = [course2]
        print(graph)

        # now look for cycle in graph
        seen = [False] * numCourses
        for course in range(numCourses):
            if self.hasCycle(course, graph, seen):
                return False
        return True

numCourses = 2 
prerequisites = [[1,0]]
print(Solution().canFinishCourse(numCourses, prerequisites))

numCourses = 2 
prerequisites = [[1,0], [0, 1]]
print(Solution().canFinishCourse(numCourses, prerequisites))