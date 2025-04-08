class SolutionStack:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        current = head
        
        # 모든 노드 값을 stack에 추가
        while current:
            stack.append(current.val)
            current = current.next
        
        current = head
        
        # stack에서 pop하면서 값 비교
        while current:
            if current.val != stack.pop():
                return False
            current = current.next
        
        return True
