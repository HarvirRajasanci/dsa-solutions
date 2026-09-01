class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "#"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"