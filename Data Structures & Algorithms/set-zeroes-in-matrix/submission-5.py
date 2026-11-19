class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_to_zero = set()
        col_to_zero = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    row_to_zero.add(r)
                    col_to_zero.add(c)

        for r in range(ROWS):
            for c in range(COLS):
                if r in row_to_zero or c in col_to_zero:
                    matrix[r][c] = 0