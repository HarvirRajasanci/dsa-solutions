class TicTacToe:

    def __init__(self, n: int):
        self.board = [["." for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = "X" if player == 1 else "O"
        return player if self._check_win(row, col, player) else 0

    def _check_win(self, row, col, player) -> bool:
        player = "X" if player == 1 else "O"
        if all(val == player for val in self.board[row]):
            return True
        elif all(row[col] == player for row in self.board):
            return True
        elif all(self.board[i][i] == player for i in range(len(self.board))):
            return True
        elif all(self.board[i][len(self.board) - 1 - i] == player for i in range(len(self.board))):
            return True
        else:
            return False
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
