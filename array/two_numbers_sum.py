# -*- coding: utf-8 -*-
# Write a program that, given an array A[] of n numbers and another number x,
# determines whether or not there exist two elements in S whose sum is exactly x.

class Solution:
    # @param A : list of list of integers
    # @param x : number with which sum to be compared
    # @return an integer
    def findElement(self, A, x):
        arr_size = len(A)
        self.merge_sort(A, 0, arr_size)

        print str(A)

        for i in range(0,arr_size):
            if(i < arr_size-1):
                if A[i] + A[i+1] == x:
                    return 1
                else:
                    continue
            return 0


    def printArray(self, A):

        for i in range(0,len(A)):
            print str(A[i])
            #for j in range(0,len(A[i])):
               # print "Element :"+ str(A[i][j])
            print "\n ***************End of Loop*********** \n"
        print "\n"

    # Implementation of Quick Sort
    # A[] --> Array to be sorted
    # si  --> Starting index
    # ei  --> Ending index
    def quickSort(self,A, si, ei):
        if si < ei:
            pi = self.partition(A, si, ei)
            self.quickSort(A, si, pi - 1)
            self.quickSort(A, pi + 1, ei)

            # Utility function for partitioning the array(used in quick sort)

    def partition(self, A, si, ei):
        x = A[ei]
        i = (si - 1)
        for j in range(si, ei):
            if A[j] <= x:
                i += 1

                # This operation is used to swap two variables is python
                A[i], A[j] = A[j], A[i]

            A[i + 1], A[ei] = A[ei], A[i + 1]

        return i + 1

    def merge_sort(self,alist, start, end):
        '''Sorts the list from indexes start to end - 1 inclusive.'''
        if end - start > 1:
            mid = (start + end) // 2
            self.merge_sort(alist, start, mid)
            self.merge_sort(alist, mid, end)
            self.merge_list(alist, start, mid, end)

    def merge_list(self,alist, start, mid, end):
        left = alist[start:mid]
        right = alist[mid:end]
        k = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end):
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid:
            while k < end:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < end:
                alist[k] = right[j]
                j = j + 1
                k = k + 1

    def main(self):
        A = [ 1, 4, 6, 10, 45]
        print(self.findElement(A,14))

if __name__ == '__main__':
    sol = Solution()
    sol.main()