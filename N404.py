"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sum_left(leftnode: TreeNode):
            if leftnode == None:
                return 0
            val_left = leftnode.val
            if leftnode.left != None:
                val_left += sum_left(leftnode.left)
            if leftnode.right != None:
                val_left += sum_right(leftnode.right)
            return val_left

        def sum_right(rightnode: TreeNode):
            if rightnode == None:
                return 0
            val_right = 0
            if rightnode.left != None:
                val_right += sum_left(rightnode.left)
            if rightnode.right != None:
                val_right += sum_right(rightnode.right)
            return val_right

        if root == None:
            return 0
        else:
            return sum_left(root.left) + sum_right(root.right)

