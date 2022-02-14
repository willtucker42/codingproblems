# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n_l = len(nums1)
        if m == 0:
            for x in range(n_l):
                nums1.pop()
            for i in nums2:
                nums1.append(i)
        else:
            if n != 0:
                x = 0
                while len(nums1) != m:
                    nums1.pop()
                x = 0
                for j in nums2:
                    inserted = False
                    for index, i in enumerate(nums1):
                        if len(nums1) == m + n:
                            break
                        if i >= j:
                            nums1.insert(index, j)
                            inserted = True
                            break
                    if not inserted:
                        nums1.append(j)

