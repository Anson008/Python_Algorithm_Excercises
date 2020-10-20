from collections import defaultdict


class Solution:
    def find_order(self, num_courses, prerequisiters):
        """
        :param num_courses: int
        :param prerequisiters: List[List[int]]
        :return: List[int]
        """
        graph = defaultdict(list)
        for p in prerequisiters:
            graph[p[0]].append(p[1])
        courses = []
        visited = [-1] * num_courses

        def dfs(u):
            visited[u] = 0
            for v in graph[u]:
                if visited[v] == 0 or (visited[v] == -1 and not dfs(v)):
                    return False
            visited[u] = 1
            courses.append(u)
            return True

        for u in range(num_courses):
            if visited[u] == -1 and not dfs(u):
                return []
        return courses
