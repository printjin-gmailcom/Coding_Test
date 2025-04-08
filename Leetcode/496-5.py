def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    return [next((nums2[j] for j in range(i + 1, len(nums2)) if nums2[j] > nums2[i]), -1)
            for i in [nums2.index(num) for num in nums1]]
