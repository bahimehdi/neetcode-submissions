class LinkedList:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.right

        return -1

    def insertHead(self, val: int) -> None:
        new = LinkedList(val)
        
        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.right = self.head
            self.head.left = new
            self.head = new

    def insertTail(self, val: int) -> None:
        new = LinkedList(val)
        if not self.tail:
            self.head = new
            self.tail = new
        else:
            self.tail.right = new
            new.left = self.tail
            self.tail = new

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                if curr == self.head:
                    self.head = curr.right
                    if self.head:
                        self.head.left = None
                    else:
                        self.tail = None

                elif curr == self.tail:
                    self.tail = curr.left
                    if self.tail:
                        self.tail.right = None
                    else:
                        self.head = None

                else:
                    curr.left.right = curr.right
                    curr.right.left = curr.left
                return True

            curr = curr.right
            i += 1

        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.right
        
        return res