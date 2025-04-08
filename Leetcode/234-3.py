class SolutionReverseHalf:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # 중간 지점 찾기
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 리스트의 두 번째 절반을 반전
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # 두 리스트의 절반 비교
        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
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