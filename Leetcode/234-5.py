class SolutionRecursive:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head
        
        def recursively_check(current_node):
            if current_node:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursively_check(head)

test_cases = [
    [1, 2, 2, 1],  # True
    [1, 2],        # False
    [1],           # True (single node)
    [],            # True (empty list)
    [1, 0, 1],     # True
]

print("\nTesting Solution with Recursion:")
for case in test_cases:
    head = create_linked_list(case)
    sol = SolutionRecursive()
    print(f"Input: {case}, Is Palindrome: {sol.isPalindrome(head)}")