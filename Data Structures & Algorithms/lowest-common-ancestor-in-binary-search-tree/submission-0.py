# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = root
        while LCA and ((LCA.val > p.val and LCA.val > q.val) or (LCA.val < p.val and LCA.val < q.val)):
            if LCA.val > p.val:
                LCA = LCA.left
            else:
                LCA = LCA.right
        return LCA