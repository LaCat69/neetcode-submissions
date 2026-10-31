"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []
        rooms = 0

        for interval in intervals:
            inserted = False
            if heap and interval.start >= heap[0]:
                heapq.heappushpop(heap, interval.end)
                inserted = True
            if not inserted:
                heapq.heappush(heap, interval.end)
                rooms += 1
            inserted = False

        return rooms