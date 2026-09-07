# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# loop 1: (slow/fast) to find the middle
# loop 2: reverse the second half
# loop 3: reorder the list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        half = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = slow.next
        slow.next = None
        reverse = None
        while secondHalf is not None:
            tmp = secondHalf.next
            secondHalf.next = reverse
            reverse = secondHalf
            secondHalf = tmp
        firstHalf = head
        secondHalf = reverse
        while secondHalf is not None:
            tmp = firstHalf.next
            tmp2 = secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next  = tmp
            firstHalf = tmp
            secondHalf = tmp2