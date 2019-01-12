# -*- coding: utf-8 -*-
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = []
        i = 0
        while (i < len(nums1)):
            if (nums1[i] in nums2):
                a.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
            i += 1
        return a






    def main(self):
        nums1 = [3,1,2]
        nums2 = [1,1]
        print self.intersect(nums1,nums2)


if __name__ == '__main__':
    sol = Solution()
    sol.main()