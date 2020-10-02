"""
    
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""


import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        pq = []
        room = 1

        heapq.heappush(pq, intervals[0][1])

        for interval in intervals[1:]:

            start, end = interval

            if start < pq[0]:
                room += 1
            else:
                heapq.heappop(pq)

            heapq.heappush(pq, end)

        return room


# soln 2
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        start = [_[0] for _ in intervals]
        end = [_[1] for _ in intervals]

        start.sort()
        end.sort()

        j = 0

        room = 1

        for idx in range(1, len(start)):
            if start[idx] >= end[j]:
                # has room available
                j += 1
            else:
                # no room
                room += 1

        return room