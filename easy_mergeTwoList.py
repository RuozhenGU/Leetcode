
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ans = ListNode(0, None)
        tmp = ans
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        
        if l1:
            tmp.next = l1
        elif l2:
            tmp.next = l2
        else:
            tmp.next = None
            
        return ans.next