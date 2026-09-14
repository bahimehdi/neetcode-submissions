# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.res = []
        self.bfs(root)
        return self.res
        

    def bfs(self, node):
        q = deque([node])

        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            self.res.append(node.val)