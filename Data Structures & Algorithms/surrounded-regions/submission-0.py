class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        safe = set()
        
        def dfs(r, c):
            if (0 > r or 0 > c or
                ROWS == r or COLS == c or
                board[r][c] == "X" or (r, c) in safe
                ):
                return

            safe.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X" 