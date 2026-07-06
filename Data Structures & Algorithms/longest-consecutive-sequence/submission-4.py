class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = sorted(set(nums))
        curr = 1
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                curr += 1
            else:
                curr = 1
            count = max(curr, count)
        
        return count