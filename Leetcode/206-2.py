from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return new_head

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
