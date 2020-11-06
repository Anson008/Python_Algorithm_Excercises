class Solution(object):
    @staticmethod
    def wall_and_gates(rooms):
        """
        Fill each empty room with the distance to its nearest gate.
        If it is impossible to reach a gate, it should be filled with INF.
        :param rooms: List[List[int]]
        :return: void
        """
        if not rooms:
            return
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        N, C = len(rooms), len(rooms[0])
        frontier = [(r, c) for r in range(N) for c in range(C) if rooms[r][c] == 0]
        INF = 2147483647
        distance = 0
        while frontier:
            next = []
            for r, c in frontier:
                for d in range(4):
                    nr, nc = r + dr[d], c + dr[d]
                    if 0 <= nr < N and 0 <= nc < C and rooms[nr][nc] == INF:
                        rooms[nr][nc] = distance + 1
                        next.append((nr, nc))
            frontier = next
            distance += 1


if __name__ == "__main__":
    pass
