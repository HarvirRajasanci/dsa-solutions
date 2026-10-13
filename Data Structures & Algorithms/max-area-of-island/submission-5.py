class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            total = 1
            for dr, dc in dirs:
                total += dfs(r + dr, c + dc)
            return total

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area