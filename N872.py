"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getleaf(self, root: TreeNode, check: list):
            if root.left == None and root.right == None:
                check.append(root.val)
            if root.left != None:
                getleaf(self, root.left, check)
            if root.right != None:
                getleaf(self, root.right, check)
        check1, check2 = [], []
        getleaf(self, root1, check1)
        getleaf(self, root2, check2)
        if check1 == check2:
            return True
        else:
            return False


r11 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
r22 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
r1 = TreeNode(r11)
r2 = TreeNode(r22)
test = Solution()
print(test.leafSimilar(r1, r2))
