class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            guess = nums[m]
            if guess == target:
                return m
            elif guess < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1