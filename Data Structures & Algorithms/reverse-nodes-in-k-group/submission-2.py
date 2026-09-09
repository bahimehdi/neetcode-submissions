# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        current = head
        while current:
            if n == k:
                break
            n += 1
            current = current.next
        newGroupHead = head
        if n < k:
            return head
        else:
            newGroupHead, nextGroupStart = self.reverseListK(newGroupHead, k)
            rest = self.reverseKGroup(nextGroupStart, k)
            head.next = rest
            return newGroupHead

    # Re-using reverse llist
    def reverseListK(self, head: Optional[ListNode], k) -> Optional[ListNode]:
        current = head
        reverse = None
        n = 0
        while current != None and n != k:
            n += 1
            tmp = current.next
            current.next = reverse
            reverse = current
            current = tmp
        return reverse, current