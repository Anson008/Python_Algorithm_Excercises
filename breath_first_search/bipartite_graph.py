class Solution(object):
    def bfs(self, graph, visited, u):
        visited[u] = 0
        frontier = [u]
        while frontier:
            next = []
            for u in frontier:
                for v in graph[u]:
                    if v not in visited:
                        visited[v] = visited[u] + 1
                        next.append(v)
                    elif visited[v] == visited[u]:
                        return False
            frontier = next
        return True

    def is_bipartite(self, graph):
        """
        :param graph: List[List[int]]
        """
        visited = {}
        for v in range(len(graph)):
            if v not in visited and not self.bfs(graph, visited, v):
                return False
        return True


if __name__ == "__main__":
    pass
