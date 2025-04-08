class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    stackA, stackB = [], []
    
    while headA:
        stackA.append(headA)
        headA = headA.next
    
    while headB:
        stackB.append(headB)
        headB = headB.next
    
    intersection = None
    while stackA and stackB and stackA[-1] == stackB[-1]:
        intersection = stackA.pop()
        stackB.pop()
    
    return intersection
