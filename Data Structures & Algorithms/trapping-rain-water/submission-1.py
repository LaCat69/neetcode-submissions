class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_height, r_height = height[l], height[r]
        total = 0

        while l < r:
            if l_height < r_height:
                total += l_height - height[l]
                l += 1
                l_height = max(l_height, height[l])
            elif l_height > r_height:
                total += r_height - height[r]
                r -= 1
                r_height = max(r_height, height[r])
            else:
                total += l_height - height[l]
                l += 1
                l_height = max(l_height, height[l])
        
        return total