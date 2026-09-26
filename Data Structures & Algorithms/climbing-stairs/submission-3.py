class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(curr):
            if curr == n:
                return 1

            if curr > n:
                return 0

            if curr in memo:
                return memo[curr]

            memo[curr] = dfs(curr + 1) + dfs(curr + 2)


            return memo[curr]

        dfs(0)
        return memo[0]