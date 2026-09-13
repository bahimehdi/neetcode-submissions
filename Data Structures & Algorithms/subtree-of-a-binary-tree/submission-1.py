# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        self.subtree = False
        self.dfs(root, subRoot)
        return self.subtree

    def dfs(self, node1, node2):
        if node1 is None or node2 is None:
            return
        if node1.val == node2.val and not self.subtree:
            self.subtree = self.sameTree(node1, node2)
        self.dfs(node1.left, node2)
        self.dfs(node1.right, node2)
    
    def sameTree(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)