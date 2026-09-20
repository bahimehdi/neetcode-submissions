class WordDictionary:

    def __init__(self, children=None, isWord=False):
        self.children = {} if children is None else children
        self.isWord = isWord
        

    def addWord(self, word: str) -> None:
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = WordDictionary()
                current = current.children[char]
        current.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(l, node):
            current = node

            for i in range(l, len(word)):
                char = word[i]
                
                if char == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
            return current.isWord

        return dfs(0, self)