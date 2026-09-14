# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dequeue to store elements
# self.elementsCount = [height0, height1,..]
# i think there is a simplification since we are working with binary trees, but idk yet

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.q = deque([root])
        self.res = []
        self.bfs()
        return self.res

    def bfs(self):
        i = 0
        while self.q:
            levelSize = len(self.q)
            self.res.append([])

            for _ in range(levelSize):
                node = self.q.popleft()
                self.res[i].append(node.val)
                if node.left:
                    self.q.append(node.left)
                if node.right:
                    self.q.append(node.right)

            i += 1