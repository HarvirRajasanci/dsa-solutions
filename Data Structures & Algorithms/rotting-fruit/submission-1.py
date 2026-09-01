class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        q = deque()
        fresh_oranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        if not fresh_oranges:
            return 0

        elapsed_time = 0
        while fresh_oranges > 0 and q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append((nr, nc))

            elapsed_time += 1

        return -1 if fresh_oranges > 0 else elapsed_time