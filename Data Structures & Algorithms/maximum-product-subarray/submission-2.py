class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        res = curr_max

        for n in nums[1:]:
            curr_min, curr_max = min(n, curr_min * n, curr_max * n), max(n, curr_min * n, curr_max * n)
            res = max(res, curr_max)
            
        return res
            
