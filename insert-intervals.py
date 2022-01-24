# You are given an array of non-overlapping intervals intervals where intervals[i] = [start-i, end-i] represent the start and the end of the ith interval 
# and intervals is sorted in ascending order by start-i. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start-i 
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Utilize merge-intervals.py

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        if n > 1:
            intervals.sort()
            i = 1
            while i < n:
                if intervals[i][0] <= intervals[i-1][1]:
                    intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                    intervals.pop(i)
                    n -=1
                else:
                    i +=1

        return intervals
