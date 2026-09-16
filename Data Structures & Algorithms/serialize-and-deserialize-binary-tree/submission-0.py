# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        self.serialized = []
        self.dfs(root)
        return ' '.join(self.serialized)

    def dfs(self, node):
        if node is None:
            self.serialized.append('#')
            return
        self.serialized.append(str(node.val))
        self.dfs(node.left)
        self.dfs(node.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == '#':
            return  None
        
        self.data = data.split(' ')
        root = TreeNode(self.data[0])
        self.preIndex = 0

        return self.build()
        
    def build(self):
        token = self.data[self.preIndex]
        self.preIndex += 1

        if token == '#':
            return None
        
        root = TreeNode(int(token))

        root.left = self.build()
        root.right = self.build()

        return root