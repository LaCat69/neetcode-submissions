class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1] * len(queries)
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        intervals.sort(key=lambda x: x[0])

        heap = []
        i = 0
        j = 0
        while i < len(sorted_queries):
            while j < len(intervals) and intervals[j][0] <= sorted_queries[i][0]:
                heapq.heappush(heap, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j += 1

            while i < len(sorted_queries) and heap and heap[0][1] < sorted_queries[i][0]:
                heapq.heappop(heap)

            if heap:
                result[sorted_queries[i][1]] = heap[0][0]
            i += 1


        return result
