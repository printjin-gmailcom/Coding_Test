from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return reverse(next_node, curr)
        
        return reverse(head, None)

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
