class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        memo = {}
        max1, max2 = 0, 0

        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
                
            memo[i] = max(arr[i] + dfs(i + 2, arr), dfs(i + 1, arr))

            return memo[i]

        dfs(0, nums[1:])
        max1 = max(memo[0], memo[1])
        memo.clear()
        dfs(0, nums[:-1])
        max2 = max(memo[0], memo[1])

        return max(max1, max2)
