class Solution:
    def dfs(self, directed_graph, visit_status, u):
        # 0 represents we are currently still visiting a node.
        # 1 represents we are done with a node.
        visit_status[u] = 0
        for v in directed_graph[u]:
            if v not in visit_status:
                if self.dfs(directed_graph, visit_status, v):
                    return True
            elif visit_status[v] == 0:
                return True
        visit_status[u] = 1
        return False

    def has_cycle(self, directed_graph):
        visit_status = {}
        for v in directed_graph:
            if v not in visit_status and self.dfs(directed_graph, visit_status, v):
                return True
        return False
