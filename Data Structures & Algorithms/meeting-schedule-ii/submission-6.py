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
        for i in range(len(intervals)):
            curr = intervals[i]
            if heap and heap[0] <= curr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, curr.end)
        return len(heap)