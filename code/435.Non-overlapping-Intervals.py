class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the right end point of the interval
        intervals.sort(key = lambda x: x[1])
        count = 0
        idx = 0
        while idx < len(intervals):
            right = intervals[idx][1]
            idx += 1
            while idx < len(intervals) and intervals[idx][0] < right:
                # remove this interval
                count += 1
                idx += 1
        return count  