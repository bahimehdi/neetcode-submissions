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
    
    def search(self, word: str):
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        root = TrieNode()
        for word in words:
            root.insert(word)

        def backtrack(row, col, trieNode, visited):
            node = trieNode.search(board[row][col])

            if (row, col) in visited or not node:
                return
            
            if node.isEnd == True:
                node.isEnd = False
                res.append(node.word)

            visited.add((row, col))
            if row < len(board) - 1:
                backtrack(row+1, col, node, visited)
            if row > 0:
                backtrack(row-1, col, node, visited)
            if col < len(board[0]) - 1:
                backtrack(row, col+1, node, visited)
            if col > 0:
                backtrack(row, col-1, node, visited)
            visited.remove((row, col))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                backtrack(row, col, root, set())
        
        return res