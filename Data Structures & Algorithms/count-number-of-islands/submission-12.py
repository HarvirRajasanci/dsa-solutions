class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()

                if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                    continue
                grid[r][c] = "0"
                for dr, dc in dirs:
                    q.append((r + dr, c + dc))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands