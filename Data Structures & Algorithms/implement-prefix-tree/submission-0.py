class PrefixTree:

    def __init__(self, children=None, isEnd=False):
        self.children = {} if children is None else children
        self.isEnd = isEnd

    def insert(self, word: str) -> None:
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                current.children[char] = PrefixTree()
                current = current.children[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.isEnd == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current = self
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True