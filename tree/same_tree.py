# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false

class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if q is not None and p is not None:
            return ((p.data == q.data) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        return False


    def isSameOptimal(self,p,q):
        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.data == q.data:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False

    def main(self):
        p=[5,1,4,None,None,3,6]
        root_p = None
        root_q = None
        for i in range(len(p)):
            if i==0:
                root_p = BinarySerchTree(p[0])
            else:
                root_p.insert(p[i])

        q=[1,2,3,4,5]
        for i in range(len(q)):
            if i==0:
                root_q = BinarySerchTree(q[0])
            else:
                root_q.insert(q[i])
        #root_p.print_tree()
        #root_q.print_tree()
        print self.isValidBST(root_p)

class BinarySerchTree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data < data:
            if self.left == None:
                self.left = BinarySerchTree(data)
            else:
                self.left.insert(data)
        elif self.left > data:
            if self.right == None:
                self.right = BinarySerchTree(data)
            else:
                self.right.insert(data)
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':
    sol = Solution()
    sol.main()




