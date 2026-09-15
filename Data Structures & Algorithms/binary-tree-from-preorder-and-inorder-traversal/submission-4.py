# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder -> node-left-right
# inorder -> left-node-right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inIndex = {
            value: i for i, value in enumerate(inorder)
        }
        self.preorder = preorder
        self.preIndex = 0
        return self.build(0, len(inorder) - 1)

        
    def build(self, inLeft, inRight):
        if inLeft > inRight:
            return None
        
        root = TreeNode(self.preorder[self.preIndex])
        self.preIndex += 1
        rootIndex = self.inIndex[root.val]

        root.left = self.build(inLeft, rootIndex - 1)
        root.right = self.build(rootIndex + 1, inRight)

        return root