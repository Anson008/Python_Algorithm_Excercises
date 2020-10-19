class Solution:
    def find_circle_num(self, M):
        ans = 0
        visited = [0] * len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(M, i, visited)
                ans += 1
        return ans

    def dfs(self, M, v, visited):
        for i in range(len(M)):
            if M[v][i] and visited[i] == 0:
                if i != v:
                    visited[i] = 1
                    self.dfs(M, i, visited)