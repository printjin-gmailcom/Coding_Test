from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        
        while head:
            next_node = head.next
            head.next = dummy.next
            dummy.next = head
            head = next_node
        
        return dummy.next

# Example usage
node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
new_head = sol.reverseList(node1)

while new_head:
    print(new_head.val)
    new_head = new_head.next
