class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            if matrix[r][0] <= target <= matrix[r][col-1]:
                left, right = 0, col-1

                while left <= right:
                    medium = (left + right) // 2
                    guess = matrix[r][medium]

                    if guess == target:
                        return True
                    elif guess < target:
                        left = medium + 1
                    else:
                        right = medium - 1
                return False
        
        return False