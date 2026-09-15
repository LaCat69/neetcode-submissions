class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        length_nums = len(nums) - 1

        def dfs(i, length):
            if i > length:
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i + 1, length)

            subset.pop()
            dfs(i + 1, length)
          
        dfs(0, length_nums)
        return res