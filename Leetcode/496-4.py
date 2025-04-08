def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    index_map = {num: i for i, num in enumerate(nums2)}
    result = []
    
    for num in nums1:
        start_index = index_map[num]
        found = False
        for i in range(start_index + 1, len(nums2)):
            if nums2[i] > num:
                result.append(nums2[i])
                found = True
                break
        if not found:
            result.append(-1)
    
    return result
