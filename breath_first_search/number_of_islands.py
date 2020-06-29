class Solution1(object):
    def bfs(self, grid, r, c, marked):
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        marked.add((r, c))
        frontier = [(r, c)]
        while frontier:
            next = []
            for r, c in frontier:
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1' \
                        and (nr, nc) not in marked:
                        node = (nr, nc)
                        marked.add(node)
                        next.append(node)
            frontier = next

    def num_islands(self, grid):
        res, marked = 0, set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in marked:
                    res += 1
                    self.bfs(grid, r, c, marked)
        return res


class Solution2(object):
    def bfs(self, grid, r, c, marker):
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        N, C = len(grid), len(grid[0])
        frontier = [r * C + c]
        while frontier:
            next = []
            for t in frontier:
                r, c = t // C, t % C
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < C and grid[nr][nc] == '1':
                        grid[nr][nc] = marker
                        next.append(nr * C + nc)
            frontier = next

    def num_islands(self, grid):
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += 1
                    self.bfs(grid, r, c, str(res + 1))
        return res