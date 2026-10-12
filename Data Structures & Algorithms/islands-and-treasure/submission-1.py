class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        CONST = 2147483647
        q = deque([])
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in seen:
                    q.append((i, j))
                    seen.add((i, j))

        level = 0
        new_q = deque([])
        while q:
            r, c = q.popleft()
            grid[r][c] = level

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS :
                    if grid[nr][nc] == CONST and (nr, nc) not in seen:
                        new_q.append((nr, nc))
                        seen.add((nr, nc))

            if not q:
                q = new_q
                new_q = deque([])
                level += 1