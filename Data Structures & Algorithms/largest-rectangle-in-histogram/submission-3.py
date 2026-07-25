class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        max_area = 0
        left = [-1] * length
        stack = []

        for l in range(length):
            while stack and heights[stack[-1]] >= heights[l]:
                stack.pop()
            if stack:
                left[l] = stack[-1]
            stack.append(l)
            

        right = [length] * length 
        stack = []
        for r in range(length-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[r]:
                stack.pop()
            if stack:
                right[r] = stack[-1]
            stack.append(r)

        for i in range(length):
            max_area = max(max_area, (right[i] - left[i] - 1) * heights[i])
        return max_area