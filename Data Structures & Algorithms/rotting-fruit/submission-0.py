class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        queue = deque()
        freshOranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        if freshOranges == 0:
            return 0

        timeElapsed = 0
        while freshOranges > 0 and queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if min(row, col) >= 0 and row < ROWS and col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        freshOranges -= 1
                        queue.append((row, col))
            timeElapsed += 1

        return -1 if freshOranges > 0 else timeElapsed

