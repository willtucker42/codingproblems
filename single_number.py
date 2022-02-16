# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i = 0
        for n in nums:
            if i == 0:
                try:
                    if nums[1] != n:
                        return n
                except:
                    return n
            else:
                try:
                    if nums[i - 1] != n and nums[i + 1] != n:
                        return n
                except:
                    return n
            i += 1
