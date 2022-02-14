# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i = 0
        c = 0
        while nums1 and nums2:
            if nums1[i] < nums2[i]:
                nums3.append(nums1[i])
                del nums1[i]
            elif nums1[i] > nums2[i]:
                nums3.append(nums2[i])
                del nums2[i]
            else:
                nums3.append(nums1[i])
                del nums1[i]
            c += 1
        if not nums1:
            for x in nums2:
                nums3.append(x)
                c += 1
        else:
            for x in nums1:
                nums3.append(x)
                c += 1
        cd2 = int(c / 2) - 1
        if c == 2:
            return (nums3[0] + nums3[1]) / 2
        if c % 2 != 0:
            return nums3[cd2 + 1]
        return (nums3[cd2] + nums3[cd2 + 1]) / 2
