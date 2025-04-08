class Solution:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2[:n]
            return
        
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            self.merge(nums1, m-1, nums2, n)
        else:
            nums1[m+n-1] = nums2[n-1]
            self.merge(nums1, m, nums2, n-1)
