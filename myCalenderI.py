"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
"""
# 最重要的就每次call book的时候，你的其实node要从root走，而在insert过程root这个node不随着traversal一起走
# 做到这件事情，你必须把你的Calender class当一个bst，在Nodeclass中insert的recursion不能写insert(root.left, start, end)
# 因为你的root不能随着动。总结，这个recursion是在node单元开始做的，不是在root、bst head开始做的。

class Node:
    def __init__(self, s, e):
        self.left = None
        self.right = None
        self.s = s
        self.e = e
        
    def insert(self, start, end):
        if start > end:
            return False
      
        if self.s >= end:
            # traverse left
            if self.left == None:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        
        if self.e <= start:
            # traverse right
            if self.right == None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        
        return False
    


class MyCalendar:

    def __init__(self):
        self.BST = None
    
    def book(self, start: int, end: int) -> bool:
        if self.BST == None:
            self.BST = Node(start, end)
            return True
        ans = self.BST.insert(start, end)
        
        return ans