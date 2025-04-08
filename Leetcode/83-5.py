class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return None
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while head:
        while head.next and head.val == head.next.val:
            head = head.next
        prev.next = head
        prev = prev.next
        head = head.next
    
    return dummy.next
