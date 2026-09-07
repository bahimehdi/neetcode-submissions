# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# traversal + not in exists set

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        current, exists = head, set()
        while current.next is not None:
            if current.val in exists:
                return True
            else:
                exists.add(current.val)
                current = current.next
        return False