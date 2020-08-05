"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root) -> bool:
        if root == None : return True
        if root.left != None and root.val != root.left.val or root.right != None and root.val != root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


