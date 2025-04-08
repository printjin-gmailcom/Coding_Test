class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print("->".join(map(str, vals)))

test_cases = [
    [1, 2, 2, 1],  # True
    [1, 2],        # False
    [1],           # True (single node)
    [],            # True (empty list)
    [1, 0, 1],     # True
]

print("Testing Solution with Stack:")
for case in test_cases:
    head = create_linked_list(case)
    sol = SolutionStack()
    print(f"Input: {case}, Is Palindrome: {sol.isPalindrome(head)}")