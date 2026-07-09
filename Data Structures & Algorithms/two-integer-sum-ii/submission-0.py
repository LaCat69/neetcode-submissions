class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            guest = numbers[l] + numbers[r]
            if guest == target:
                return [l+1, r+1]
            elif guest < target:
                l += 1
            else:
                r -= 1