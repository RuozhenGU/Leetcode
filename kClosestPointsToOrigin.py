"""

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
"""


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def divide_and_conquer(l, r, points, k):

            if r - l + 1 >= k:  # this is base case, includes l >= r

                idx = partition(l, r, points)
                if idx - l + 1 == k:
                    return points[0 : idx + 1]

                if idx - l + 1 > k:
                    return divide_and_conquer(l, idx - 1, points, k)
                else:
                    return divide_and_conquer(idx + 1, r, points, k - (idx - l + 1))

        def partition(l, r, points):

            i = l
            pivot = dist(r)

            for j in range(i, r):
                if dist(j) < pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                else:
                    continue

            points[i], points[r] = points[r], points[i]

            return i

        return divide_and_conquer(0, len(points) - 1, points, K)
