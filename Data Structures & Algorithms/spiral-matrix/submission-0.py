class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        res = []

        while right > left and down > up:
            for i in range(left, right):
                res.append(matrix[up][i])

            up += 1

            if down == up:
                break

            for j in range(up, down):
                res.append(matrix[j][i])

            right -= 1
            if right == left:
                break

            for x in range(right-1, left-1, -1):
                res.append(matrix[j][x])

            down -= 1
            if down == up:
                break

            for y in range(down-1, up-1, -1):
                res.append(matrix[y][left])

            left += 1
            if right == left:
                break

            
        return res