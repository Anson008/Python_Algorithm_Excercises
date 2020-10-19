from collections import defaultdict


class Solution:
    def has_cycle(self, graph, visited, parent, u):
        visited.add(u)
        for v in graph[u]:
            if v != parent:
                if v in visited or self.has_cycle(graph, visited, u, v):
                    return True
        return False

    def valid_tree(self, n, edges):
        """
        :param n: int
        :param edges: List[List[int]]
        """
        visited = set()
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return not self.has_cycle(graph, visited, -1, 0) and len(visited) == n