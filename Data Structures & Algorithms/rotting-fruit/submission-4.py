class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        fresh_fruits = 0
        seen = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))

        minutes = 0
        if not fresh_fruits:
            return 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            level = deque([])
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1 and (nr, nc) not in seen:
                            fresh_fruits -= 1
                            level.append((nr, nc))
                            seen.add((nr, nc))
            minutes += 1
            q = level
            if fresh_fruits == 0:
                return minutes

        return minutes if fresh_fruits == 0 else -1