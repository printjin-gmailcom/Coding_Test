class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        vals = []
        current = head
        
        while current:
            if current.val != val:
                vals.append(current.val)
            current = current.next
        
        dummy = ListNode(0)
        current = dummy
        
        for v in vals:
            current.next = ListNode(v)
            current = current.next
        
        return dummy.next
