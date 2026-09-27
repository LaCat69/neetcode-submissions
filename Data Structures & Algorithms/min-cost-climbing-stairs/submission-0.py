class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        dfs(0)

        return min(memo[0], memo[1])