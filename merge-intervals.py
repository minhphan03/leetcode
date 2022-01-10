# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # replicate an improved solution version from Amrutha_BS
        
        intervals.sort()
        i = 1
        n = len(intervals)
        while i < n:
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                intervals.pop(i)
                n -=1
            else:
                i +=1
        
        return intervals
