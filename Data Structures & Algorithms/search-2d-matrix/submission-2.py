class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            medium = (left + right) // 2
            row = medium // cols
            col = medium % cols

            guess = matrix[row][col]
            if guess == target:
                return True
            elif guess < target:
                left = medium + 1
            else:
                right = medium - 1
        
        return False