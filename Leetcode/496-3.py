def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for num in nums1:
        found = False
        for i in range(len(nums2)):
            if nums2[i] == num:
                found = True
            if found and nums2[i] > num:
                result.append(nums2[i])
                break
        else:
            result.append(-1)
    return result
