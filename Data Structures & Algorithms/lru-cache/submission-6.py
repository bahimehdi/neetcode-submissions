class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = {}
        self.right = Node()
        self.left = Node()
        self.right.prev = self.left
        self.left.nxt = self.right

    def get(self, key: int) -> int:
        if key in self.pairs:
            MRU = self.pairs[key]
            MRU.prev.nxt = MRU.nxt
            MRU.nxt.prev = MRU.prev
            MRU.nxt = self.right
            MRU.prev = self.right.prev
            self.right.prev.nxt = MRU
            self.right.prev = MRU
            return MRU.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            self.pairs[key].val = value
            MRU = self.pairs[key]
            MRU.prev.nxt = MRU.nxt
            MRU.nxt.prev = MRU.prev
            MRU.nxt = self.right
            MRU.prev = self.right.prev
            self.right.prev.nxt = MRU
            self.right.prev = MRU
            return
        # we delete the MRU
        if len(self.pairs) == self.capacity:
            del self.pairs[self.left.nxt.key]
            self.left.nxt = self.left.nxt.nxt
            self.left.nxt.prev = self.left
            self.put(key, value)
        else:
            self.pairs[key] = Node(key, value, self.right, self.right.prev)
            MRU = self.pairs[key]
            self.right.prev.nxt = MRU
            self.right.prev = MRU
            return

class Node:
    def __init__(self, key=None, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev