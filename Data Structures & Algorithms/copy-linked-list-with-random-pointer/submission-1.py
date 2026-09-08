"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# create deep copy of the list
# consists of n new nodes. Each one respects:
# contains the original `val` of the copied node
# a `next` pointer to the new node corresponding to the `next` pointer of the original node
# a `random` pointer to the new node corresponding to the `random` pointer of the original node
# Rule:
# None of the pointers of the new list should point to nodes in the original list
# Output:
# return the head of the copied linked list

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = Node(0)
        copyCurrent = copy
        current = head
        randoms = {}
        # to create a complelty new copy, we must re-create the nodes
        # loop to store .val and .next
        while current:
            copyCurrent.next = Node(current.val)
            copyCurrent = copyCurrent.next
            randoms[current] = copyCurrent
            current = current.next

        current = head
        copyCurrent = copy.next
        # loop to store .random
        while current:
            if current.random:
                copyCurrent.random = randoms[current.random]
            else:
                copyCurrent.random = None
            copyCurrent = copyCurrent.next
            current = current.next

        return copy.next