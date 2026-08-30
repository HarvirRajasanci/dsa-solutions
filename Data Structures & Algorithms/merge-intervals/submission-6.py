class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        i = 1
        while i < len(intervals):
            start, end = intervals[i]
            prev_start, prev_end = intervals[i - 1]

            if start <= prev_end:
                intervals[i-1][1] = max(prev_end, end)
                intervals.pop(i)
            else:
                i += 1

        return intervals
