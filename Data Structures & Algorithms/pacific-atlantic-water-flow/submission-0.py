class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, visit, prev):
            if ((r, c) in visit or
                    r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    heights[r][c] < prev
                ):
                    return

            visit.add((r, c))
            for dr, dc in directions:
                dfs(dr + r, dc + c, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacific , 0)
        for c in range(COLS):
            dfs(0, c, pacific, 0)
        for r in range(ROWS):
            dfs(r, COLS-1, atlantic, 0)
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic, 0)

        res = []

        for pair in pacific:
            if pair in atlantic:
                res.append(list(pair))

        return res