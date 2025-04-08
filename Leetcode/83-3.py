class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    seen = []
    dummy = ListNode(0)
    current = dummy
    
    while head:
        if head.val not in seen:
            seen.append(head.val)
            current.next = ListNode(head.val)
            current = current.next
        head = head.next
    
    return dummy.next
