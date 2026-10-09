class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    queue = deque([(row, col)])
                    count = 1
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if (0 <= nr < ROWS and
                                0 <= nc < COLS and 
                                grid[nr][nc] == 1 and
                                (nr, nc) not in visited):
                                queue.append((nr, nc))
                                visited.add((nr, nc))
                                count += 1
                    res = max(count, res)

        return res