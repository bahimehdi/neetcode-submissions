class TrieNode:

    def __init__(self, children=None, isEnd=False):
        self.children = {} if children is None else children
        self.isEnd = isEnd
        self.word = ""

    def insert(self, word: str) -> None:
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
        current.isEnd = True
        current.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        root = TrieNode()
        for word in words:
            root.insert(word)
            
        visited = set()
        def backtrack(row, col, trieNode):
            if (row, col) in visited:
                return
            
            if board[row][col] in trieNode.children:
                node = trieNode.children[board[row][col]]
            else:
                return
            
            if node.isEnd == True:
                node.isEnd = False
                res.append(node.word)

            visited.add((row, col))
            if row < len(board) - 1:
                backtrack(row+1, col, node)
            if row > 0:
                backtrack(row-1, col, node)
            if col < len(board[0]) - 1:
                backtrack(row, col+1, node)
            if col > 0:
                backtrack(row, col-1, node)
            visited.remove((row, col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(row, col, root)
        
        return res