class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = nums[0]

        for n in nums[1:]:
            num ^= n
        
        return num