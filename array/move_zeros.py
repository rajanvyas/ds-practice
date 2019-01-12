# -*- coding: utf-8 -*-
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.




class Solution(object):

    ## Approach 1 : Here we create a parallel array of same size with default element as 0
    # and move non zero elements from left of its index, remaining elements will be 0 anyways
    # pros : time complexity becomes O(N)
    # cons : double the space is required to hold parallel array


    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        array_size = len(nums)
        result_array = [0]*array_size

        print result_array
        index = 0
        for i in range(array_size):
            if nums[i] != 0:
                result_array[index] = nums[i]
                index+=1
            else:
                continue
        return result_array

    ## Approach 2 : traverse through the array and swap the zeros till it becomes the last elements
    # pros : less space required, time complexity is O(N)
    # cons : don't see any, if you find one please write the comments
    ##

    def moveZerosOptimal(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                continue
            if i - count >= 0:
                nums[i], nums[i - count] = nums[i - count], nums[i]
        return nums




    def main(self):
        A = [0,1,0,3,12]
        print self.moveZeroes(A)
        B = [0,1,0,3,12]
        print self.moveZerosOptimal(B)

if __name__ == '__main__':
    sol = Solution()
    sol.main()