# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = root.val
        self.dfs(root)
        return self.maximum

    def dfs(self, node):
        if node is None:
            return 0
        leftReport = self.dfs(node.left)
        rightReport = self.dfs(node.right)
        maxima = max(node.val, node.val + leftReport, node.val + rightReport)

        self.maximum = max(self.maximum, maxima, node.val + leftReport + rightReport)
        return maxima