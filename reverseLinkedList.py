class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        curr = head
        while curr.next: 
            curr = curr.next
        
        def helper(head):
            if head.next == None:
                return head
            else:
                tmp = helper(head.next)
                tmp.next = head
                head.next = None  # to prevent cycle! IMPORTANT
                return head
            
        helper(head)
        
        return curr