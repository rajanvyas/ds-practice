# -*- coding: utf-8 -*-
# Given a binary array, we can flip all the 1 are in the left part and all the 0 to the right part.Calculate the minimum flips required to make all 1s in left and all 0s in right.
#
# Examples:
#
# Input: 1011000
# Output: 1
# 1 flip is required to make it 1111000.
#
# Input : 00001
# Output : 2
# 2 flips required to make it 10000.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findNumberofFlips(self, A):

        array_size = len(A)
        count = 0
        expected = '1'
        for i in range(array_size):
            if(A[i] != expected):
                count +=1
            expected = self.flip(expected)

        print count





    def flip(self,ch):
        if ch == '0':
            return '1'
        else:
            return '0'



    def main(self):
        A='1011000'
        print str(self.findNumberofFlips(A))

if __name__ == '__main__':
    sol=Solution()
    sol.main()