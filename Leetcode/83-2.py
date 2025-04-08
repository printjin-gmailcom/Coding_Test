class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    head.next = deleteDuplicates(head.next)
    return head if head.val != head.next.val else head.next
