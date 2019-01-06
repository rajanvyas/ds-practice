# -*- coding: utf-8 -*-

# Find the longest increasing subsequence of a given sequence / array.
# In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order,
# and in which the subsequence is as long as possible.
# This subsequence is not necessarily contiguous, or unique.
# In this case, we only care about the length of the longest increasing subsequence.
#
# Example :
#
# Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output : 6
# The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):

        length = len(A)

        subsequence = [1]*length



        for i in range(1,length):
            for j in range(0,i):
                if A[i] > A[j] and subsequence[i] < (subsequence[j] + 1):
                    subsequence[i] = subsequence[j]+1
        maximum = 0
        for i in range(length):
            maximum = max(maximum,subsequence[i])

        return maximum

    def main(self):
        #A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        A=[10, 22, 9, 33, 21, 50, 41, 60]
        print str(self.lis(A))

if __name__ == '__main__':
    sol=Solution()
    sol.main()

