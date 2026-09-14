# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        self.isBst = True
        self.bst(root, float('-inf'), float('inf'))
        return self.isBst
        
    def bst(self, node, lower, upper):
        if node is None:
            return
        if node.val > lower and node.val < upper:
            if node.right:
                self.bst(node.right, max(lower, node.val), upper)
            if node.left:
                self.bst(node.left, lower, min(upper, node.val))
        else:
            self.isBst = False