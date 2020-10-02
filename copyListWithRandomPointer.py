
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

"""


# solve like a graph
class Solution:
    
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head] # it saves the copied node
        
        new_node = Node(head.val, None, None)
        
        self.visited[head] = new_node
        
        head_ptr = head
            
        new_node.next = self.copyRandomList(head_ptr.next)
        new_node.random = self.copyRandomList(head_ptr.random)
        
        return new_node