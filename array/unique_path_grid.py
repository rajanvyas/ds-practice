# -*- coding: utf-8 -*-
#  Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance,
#  if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Example :
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):

        paths = [[0] * len(A[0]) for i in A]

        self.printArray(paths)
        print "\n"

        if A[0][0] == 0:
            paths[0][0] = 1

        for column in range(1,len(A)):
            if A[column][0] == 0:
                paths[column][0] = paths[column-1][0]
        n = len(A[0])
        for row in range(1,n):
            if A[0][row]==0:
                paths[0][row]=paths[0][row-1]
        self.printArray(paths)

        for x in range(1,len(A)):
            for y in range(1,len(A[x])):
                if A[x][y] == 0:
                    paths[x][y] = paths[x-1][y] + paths[x][y-1]
                    print str(paths[x][y])+" = "+str(paths[x-1][y])+" + " + str(paths[x][y-1])

        self.printArray(paths)

        return paths[-1][-1]

    def printArray(self, A):

        for i in range(0,len(A)):
            print str(A[i])
            #for j in range(0,len(A[i])):
               # print "Element :"+ str(A[i][j])
            print "\n ***************End of Loop*********** \n"
        print "\n"


    def findObstacle(self,elem):
        if elem is 1:
            return True
        else :
            return False


    def main(self):
        A = [[0,0,0],[0,1,0],[0,0,0]]
        print(self.uniquePathsWithObstacles(A))

if __name__ == '__main__':
    sol = Solution()
    sol.main()