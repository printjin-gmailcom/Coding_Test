class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
