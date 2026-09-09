# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        previousGroupTail = dummy
        while previousGroupTail:
            kth = previousGroupTail
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next
            groupStart = previousGroupTail.next
            nextGroupStart = kth.next
            newGroupHead, _ = self.reverseListK(groupStart, k)
            previousGroupTail.next = newGroupHead
            groupStart.next = nextGroupStart
            previousGroupTail = groupStart

    # Re-using reverse llist
    def reverseListK(self, head: Optional[ListNode], k):
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