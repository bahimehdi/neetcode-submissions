# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.res = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, node, pathMax):
        if node is None:
            return
        if pathMax <= node.val:
            self.res += 1
        if node.right:
            self.dfs(node.right, max(pathMax, node.right.val))
        if node.left:
            self.dfs(node.left, max(pathMax, node.left.val))