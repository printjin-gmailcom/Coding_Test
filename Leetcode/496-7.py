import bisect

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    sorted_nums2 = sorted(nums2)
    result = []
    
    for num in nums1:
        pos = bisect.bisect_right(sorted_nums2, num)
        if pos < len(sorted_nums2):
            result.append(sorted_nums2[pos])
        else:
            result.append(-1)
    
    return result
