class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            next_dp = dp.copy()
            for n in dp:
                if nums[i] + n == total // 2:
                    return True
                next_dp.add(nums[i] + n)
            dp = next_dp
        
        return False