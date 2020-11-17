"""
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

You may only use constant extra space. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

# very well explained : https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/solution/

# basically do not use left right to find next level node in queue, but instead when on level i, form the next pointer for level i+1
# then use next pointer to traverse level i + 1 to replace a queue
# so problem becomes how to set next pointer for i + 1 while you are on level i
# basically you keep track the leftmost node of next level, and each time on level i, you go to the right node, check its left and right
# children. if has a left, then leftmost.next = it. if no left but right then leftmost.next = it. if both exist,
# then left.most.next = my left and myleft.next = myright.next. if no children, no update, just go to next node on i th level

# treat tree as a linked list
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":

        if root == None:
            return root

        curr, leftmost = root, None

        next_level_curr = None

        while curr:

            if curr.left:

                if not next_level_curr:
                    next_level_curr = curr.left
                    leftmost = curr.left  # start of the next level
                else:
                    next_level_curr.next = curr.left
                    next_level_curr = curr.left

            if curr.right:

                if not next_level_curr:
                    next_level_curr = curr.right
                    leftmost = curr.right
                else:
                    next_level_curr.next = curr.right
                    next_level_curr = curr.right

            if curr.next == None:
                # next level
                curr = leftmost
                leftmost = None
                next_level_curr = None
            else:
                curr = curr.next
        return root