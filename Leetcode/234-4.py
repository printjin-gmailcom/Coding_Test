class SolutionTwoPointer:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # 리스트를 배열로 변환
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        
        # 두 포인터를 이용한 회문 체크
        left, right = 0, len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        
        return True

test_cases = [
    [1, 2, 2, 1],  # True
    [1, 2],        # False
    [1],           # True (single node)
    [],            # True (empty list)
    [1, 0, 1],     # True
]

print("\nTesting Solution with Two Pointers:")
for case in test_cases:
    head = create_linked_list(case)
    sol = SolutionTwoPointer()
    print(f"Input: {case}, Is Palindrome: {sol.isPalindrome(head)}")