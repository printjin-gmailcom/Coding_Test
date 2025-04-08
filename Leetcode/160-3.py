class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    visited = set()
    while headA:
        visited.add(headA)
        headA = headA.next
    while headB:
        if headB in visited:
            return headB
        headB = headB.next
    return None
