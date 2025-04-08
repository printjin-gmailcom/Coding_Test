class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    while headA != headB:
        headA = headA.next
        headB = headB.next
    
    return headA
