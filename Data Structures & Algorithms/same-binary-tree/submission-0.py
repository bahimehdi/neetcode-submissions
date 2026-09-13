# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equivalent = True
        self.dfs(p, q)
        return self.equivalent

    def dfs(self, p, q):
        if not self.equivalent:
            return
        if p is not None and q is not None:
            if p.val != q.val:
                self.equivalent = False
            self.dfs(p.left, q.left)
            self.dfs(p.right, q.right)
            return
        elif (p is None and q is not None) or (p is not None and q is None):
            self.equivalent = False