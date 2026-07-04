class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        prefix[0] = 1

        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1] 
        
        sufix = 1
        for i in range(length-1, -1, -1):
            prefix[i] = sufix * prefix[i]
            sufix *= nums[i]

        return prefix