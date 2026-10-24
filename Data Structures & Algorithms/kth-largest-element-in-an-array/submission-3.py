class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if heap[0] < n:
                heapq.heappushpop(heap, n)

        return heap[0]