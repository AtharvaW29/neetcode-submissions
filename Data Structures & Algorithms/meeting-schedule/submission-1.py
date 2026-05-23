"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        temp_e = -float('inf')
        for interval in intervals:
            if interval.start >= temp_e:
                temp_e = max(interval.end, temp_e)
            else:
                return False
        return True