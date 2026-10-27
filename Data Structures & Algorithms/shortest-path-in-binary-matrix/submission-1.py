class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1))

        if grid[0][0] != 0:
            return -1

        visited = set([(0, 0)])
        q = deque([(0, 0, 1)])

        while q:
            size = len(q)
            for i in range(size):
                row, col, depth = q.popleft()

                if (row, col) == (ROWS - 1, COLS - 1):
                    return depth

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 0 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc, depth + 1))

        return -1
