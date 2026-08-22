class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        output = []
        l = r = 0

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)    

            if dq[0] < l:
                dq.popleft()

            if r - l + 1 == k:
                output.append(nums[dq[0]])
                l += 1

            r += 1

        return output