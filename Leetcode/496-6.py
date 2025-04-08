def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    return [next_greater.get(num, -1) for num in nums1]
