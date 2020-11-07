class GraphNode:
    def __init__(self, key):
        self.key = key
        self.neighbor = []


class Solution:
    def copy(self, graph):
        if graph is None:
            return
        new_graph_map = {}
        res = []
        for node in graph:
            node_copy = self.dfs(node, new_graph_map)
            res.append(node_copy)
        return res

    def dfs(self, node, new_graph_map):
        if node in new_graph_map:
            return new_graph_map[node]
        output = GraphNode(node.key)
        output.key = node.key
        new_graph_map[node] = output
        for neighbor in node.neighbors:
            output.neighbors.append(self.dfs(neighbor, new_graph_map))
        return output