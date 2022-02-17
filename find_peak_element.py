# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

class Solution(object):
    def findPeakElement(self, nums):
        len_ = len(nums)
        if len_ > 1:
            for i in range(len_):
                if i == 0:
                    if nums[i] > nums[i + 1]:
                        return i
                elif i == len_ - 1:
                    if nums[i] > nums[i - 1]:
                        return i
                else:
                    if nums[i - 1] < nums[i] > nums[i + 1]:
                        return i
        else:
            return 0

        
