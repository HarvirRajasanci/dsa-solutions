class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        i = 1
        while i < len(intervals):
            curr = intervals[i]
            prev = intervals[i-1]
            
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
                intervals.pop(i)
            else:
                i += 1
        return intervals