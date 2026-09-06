class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removes = 0

        i = 1
        while i < len(intervals):
            curr = intervals[i]
            prev = intervals[i - 1]

            if prev[1] > curr[0]:
                intervals.pop(i)
                removes += 1
            else:
                i += 1

        return removes


        