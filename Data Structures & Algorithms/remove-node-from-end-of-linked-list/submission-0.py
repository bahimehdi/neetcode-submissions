# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy
        counter = 0
        while fast and fast.next:
            if counter >= n:
                slow = slow.next
            counter += 1
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next