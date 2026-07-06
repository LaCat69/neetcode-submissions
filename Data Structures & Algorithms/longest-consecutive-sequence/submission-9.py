class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        curr = 1
        count = 0

        for n in arr:
            if not n - 1 in arr:
                while n + 1 in arr:
                    curr += 1
                    n += 1
                count = max(count, curr)
                curr = 1
            
        return count