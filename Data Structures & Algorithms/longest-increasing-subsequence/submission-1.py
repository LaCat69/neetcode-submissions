class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = len(nums) * [1]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)