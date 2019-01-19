# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#
# Input:
#     2
#    / \
#   1   3
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

class Solution(object):
    class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            prev = [None]

            return self.helper(root, prev)

        def helper(self, root, prev):
            if root == None:
                return True
            if not self.helper(root.left, prev):
                return False
            if prev[0] >= root.val:
                return False

            prev[0] = root.val

            return self.helper(root.right, prev)


    def main(self):
        p=[5,1,4,None,None,3,6]
        root_p = None

        for i in range(len(p)):
            if i==0:
                root_p = BinarySerchTree(p[0])
            else:
                root_p.insert(p[i])
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
