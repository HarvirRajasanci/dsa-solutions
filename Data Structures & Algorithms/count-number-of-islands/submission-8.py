class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c, grid):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r + dr, c + dc, grid)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c, grid)
                    islands += 1

        return islands