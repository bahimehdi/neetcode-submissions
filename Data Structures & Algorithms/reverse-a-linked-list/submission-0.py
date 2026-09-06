# just append the current ListNode to the beginning each time

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse = None
        if current is None or current.next is None:
            return current
        while current != None:
            tmp = current.next
            current.next = reverse
            reverse = current
            current = tmp
        return reverse