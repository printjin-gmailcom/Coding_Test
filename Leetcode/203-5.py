class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        
        current = head
        
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head if head.val != val else head.next
