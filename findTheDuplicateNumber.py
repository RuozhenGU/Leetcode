"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

    How can we prove that at least one duplicate number must exist in nums? 
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?

"""

"""
Here's my understanding of the Floyd's Tortoise and Hare solution, and the analysis of its time complexity.

First of all, when traversing the array described in the problem by always using the current value as the next 
index to go to, there must be a loop. Let's say C is the length of the loop, which is smaller than the size of the 
array, aka C < n + 1. Before entering the loop, there are K steps to get from nums[0] to the beginning of the loop.
 Apparently, K is also smaller than the size of the array, aka K < n + 1.

Now let's see what's happening during the first loop. When Tortoise/Slow first reached the beginning of the loop, 
it moved K times; Meanwhile, Hare/Fast moved K times past the beginning of the loop, and is now somewhere in the loop.
 We could take note of Fast's current distance from the beginning of the loop, which is (K % C). At this point, 
 how many moves it would take for Fast to catch up with Slow within the loop? It would surely take less than C moves.
  In fact, with each move, Fast would shorten the gap of the two by one. We know Fast is (K % C) steps ahead of the 
  start point of the loop, so the gap between the two is (C - (K % C)). This is to say, When Fast catches Slow, 
  aka the first loop exits, Slow has moved (C - (K % C)) steps past the beginning of the loop.

Time complexity of the first loop: Slow moved K times before the loop, and then less than one loop to be caught up.
 O(K + C) = O(n).

And then we move to the second loop. Slow's position remains the same while Fast is reset to nums[0]. 
Also Fast now moves at the same speed as Slow does. If Fast and Slow were to meet, they should meet at the beginning 
of the loop. Now would they? Let's take a look. It would take Fast K moves to get to the beginning of the loop. 
Where would Slow be after K moves? It would be (C - (K % C) + K) steps past the beginning of the loop. Where the 
hell is that? Let's mod it with C: (C - (K % C) + K) % C = (C % C) - ((K % C) % C) + (K % C) = 0 - (K % C) + (K % C)
 = 0. So yes, after K moves, Slow is also at the beginning of the loop. Thus, it would take exactly K moves to exit
  the second loop, and we found the beginning of the loop.

Time complexity of the second loop: O(K) = O(n).
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        # frame 1: find if there are actually loops
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        # frame 2: find beginning of cycle/loop
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare