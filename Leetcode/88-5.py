import heapq

class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = list(heapq.merge(nums1[:m], nums2))
