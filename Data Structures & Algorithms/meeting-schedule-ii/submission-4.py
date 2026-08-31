"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        heap = []

        for intervals in intervals:
            if heap and heap[0] <= intervals.start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals.end)
        return len(heap)
