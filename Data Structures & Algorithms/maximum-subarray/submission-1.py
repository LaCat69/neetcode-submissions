class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_count = 0
        max_count = float("-inf")
        for i in range(len(nums)):
            curr_count += nums[i]
            max_count = max(max_count, curr_count)
            if curr_count < 0:
                curr_count = 0

        return max_count